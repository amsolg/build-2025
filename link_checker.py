#!/usr/bin/env python3

import re
import os
import sys
import requests
import concurrent.futures
from pathlib import Path
from urllib.parse import urlparse

# Regular expression for finding URLs in markdown files
URL_PATTERN = r'(https?://[^\s()<>"\']+)'

def find_markdown_files(base_path):
    """Find all markdown files in the repository"""
    markdown_files = []
    for root, _, files in os.walk(base_path):
        for file in files:
            if file.lower().endswith('.md'):
                markdown_files.append(os.path.join(root, file))
    return markdown_files

def extract_urls_from_file(file_path):
    """Extract URLs from a markdown file"""
    with open(file_path, 'r', encoding='utf-8') as f:
        content = f.read()
    
    urls = []
    for line_number, line in enumerate(content.split('\n'), 1):
        for match in re.finditer(URL_PATTERN, line):
            url = match.group(0)
            # Ensure URL doesn't end with punctuation
            if url[-1] in '.,:;)]}':
                url = url[:-1]
            urls.append((url, line_number))
    
    return file_path, urls

def check_url(url):
    """Check if a URL is reachable"""
    try:
        # Parse the URL to avoid unnecessary requests to invalid URLs
        parsed_url = urlparse(url)
        if not all([parsed_url.scheme, parsed_url.netloc]):
            return url, False, "Invalid URL format"
        
        # Make a HEAD request first (faster, less bandwidth)
        response = requests.head(url, timeout=10, allow_redirects=True)
        
        # If HEAD request fails with method not allowed, try GET
        if response.status_code >= 400:
            response = requests.get(url, timeout=10, stream=True, allow_redirects=True)
            # Close the connection without downloading the content
            response.close()
            
        return url, response.status_code < 400, str(response.status_code)
    except requests.exceptions.RequestException as e:
        return url, False, str(e)

def main():
    base_path = os.path.dirname(os.path.abspath(__file__))
    markdown_files = find_markdown_files(base_path)
    
    print(f"Found {len(markdown_files)} markdown files to check.")
    
    # Extract URLs from all files
    all_urls = []
    for file_path in markdown_files:
        path, urls = extract_urls_from_file(file_path)
        for url, line_number in urls:
            all_urls.append((url, path, line_number))
    
    unique_urls = set(url for url, _, _ in all_urls)
    print(f"Found {len(unique_urls)} unique URLs to check.")
    
    # Check URLs in parallel
    url_status = {}
    with concurrent.futures.ThreadPoolExecutor(max_workers=10) as executor:
        future_to_url = {executor.submit(check_url, url): url for url in unique_urls}
        for future in concurrent.futures.as_completed(future_to_url):
            url = future_to_url[future]
            try:
                url, is_reachable, status = future.result()
                url_status[url] = (is_reachable, status)
                if not is_reachable:
                    print(f"Broken link: {url} - {status}")
            except Exception as e:
                url_status[url] = (False, str(e))
                print(f"Error checking {url}: {str(e)}")
    
    # Generate report
    broken_links = []
    for url, path, line_number in all_urls:
        is_reachable, status = url_status[url]
        if not is_reachable:
            broken_links.append((path, line_number, url, status))
    
    # Sort broken links by file path
    broken_links.sort(key=lambda x: x[0])
    
    # Generate report
    report = ["# Broken Links Report\n"]
    report.append(f"Total URLs checked: {len(unique_urls)}")
    report.append(f"Total broken links found: {len(broken_links)}\n")
    
    current_file = None
    for path, line_number, url, status in broken_links:
        rel_path = os.path.relpath(path, base_path)
        if rel_path != current_file:
            report.append(f"\n## {rel_path}")
            current_file = rel_path
        
        report.append(f"- Line {line_number}: [{url}]({url}) - Status: {status}")
    
    # Write report to file
    with open(os.path.join(base_path, 'broken_links_report.md'), 'w', encoding='utf-8') as f:
        f.write('\n'.join(report))
    
    print(f"\nReport generated: broken_links_report.md")
    print(f"Total broken links found: {len(broken_links)}")

if __name__ == "__main__":
    main()