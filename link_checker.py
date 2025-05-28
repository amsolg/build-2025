#!/usr/bin/env python3
"""
Link Checker for Microsoft Build 2025 Repository

This script scans all markdown files in the repository for URLs and tests each one
for reachability. It generates a detailed report of broken links.
"""

import os
import sys
import re
import requests
from urllib.parse import urlparse, urljoin
from pathlib import Path
import time
from datetime import datetime

class LinkChecker:
    def __init__(self, root_dir='.', timeout=10, max_retries=2):
        self.root_dir = Path(root_dir)
        self.timeout = timeout
        self.max_retries = max_retries
        self.session = requests.Session()
        self.session.headers.update({
            'User-Agent': 'Mozilla/5.0 (compatible; LinkChecker/1.0; +https://github.com/amsolg/build-2025)'
        })
        self.broken_links = []
        self.checked_urls = {}  # Cache to avoid duplicate checks
        
    def find_markdown_files(self):
        """Find all markdown files in the repository."""
        md_files = []
        for file_path in self.root_dir.rglob('*.md'):
            if '.git' not in str(file_path):
                md_files.append(file_path)
        return md_files
    
    def extract_urls_from_file(self, file_path):
        """Extract all URLs from a markdown file."""
        try:
            with open(file_path, 'r', encoding='utf-8') as f:
                content = f.read()
        except Exception as e:
            print(f"Error reading {file_path}: {e}")
            return []
        
        # Regex patterns for different URL formats in markdown
        patterns = [
            r'\[([^\]]*)\]\(([^)]+)\)',  # [text](url)
            r'<(https?://[^>]+)>',       # <url>
            r'(?:^|[\s])https?://[^\s]+', # standalone URLs
        ]
        
        urls = []
        line_number = 0
        
        for line_num, line in enumerate(content.split('\n'), 1):
            for pattern in patterns:
                matches = re.finditer(pattern, line)
                for match in matches:
                    if pattern == r'\[([^\]]*)\]\(([^)]+)\)':
                        url = match.group(2)
                        text = match.group(1)
                    elif pattern == r'<(https?://[^>]+)>':
                        url = match.group(1)
                        text = url
                    else:
                        url = match.group(0).strip()
                        text = url
                    
                    # Skip relative links and anchors
                    if url.startswith('http'):
                        urls.append({
                            'url': url,
                            'text': text,
                            'line': line_num,
                            'file': str(file_path.relative_to(self.root_dir))
                        })
        
        return urls
    
    def check_url(self, url):
        """Check if a URL is reachable."""
        if url in self.checked_urls:
            return self.checked_urls[url]
        
        print(f"Checking: {url}")
        
        for attempt in range(self.max_retries + 1):
            try:
                # Handle special cases
                parsed = urlparse(url)
                if parsed.netloc in ['localhost', '127.0.0.1']:
                    self.checked_urls[url] = False
                    return False
                
                response = self.session.head(url, timeout=self.timeout, allow_redirects=True)
                
                # If HEAD fails, try GET
                if response.status_code >= 400:
                    response = self.session.get(url, timeout=self.timeout, allow_redirects=True)
                
                is_ok = response.status_code < 400
                self.checked_urls[url] = is_ok
                
                if not is_ok:
                    print(f"  ❌ Failed: {response.status_code}")
                else:
                    print(f"  ✅ OK: {response.status_code}")
                
                return is_ok
                
            except requests.exceptions.RequestException as e:
                if attempt < self.max_retries:
                    print(f"  Retry {attempt + 1}/{self.max_retries}: {e}")
                    time.sleep(1)
                else:
                    print(f"  ❌ Error: {e}")
                    self.checked_urls[url] = False
                    return False
        
        return False
    
    def check_all_links(self):
        """Check all links in all markdown files."""
        md_files = self.find_markdown_files()
        print(f"Found {len(md_files)} markdown files to check")
        
        total_urls = 0
        
        for file_path in md_files:
            print(f"\nChecking file: {file_path.relative_to(self.root_dir)}")
            urls = self.extract_urls_from_file(file_path)
            total_urls += len(urls)
            
            for url_info in urls:
                if not self.check_url(url_info['url']):
                    self.broken_links.append(url_info)
        
        print(f"\nSummary:")
        print(f"- Total markdown files: {len(md_files)}")
        print(f"- Total URLs checked: {total_urls}")
        print(f"- Unique URLs checked: {len(self.checked_urls)}")
        print(f"- Broken links found: {len(self.broken_links)}")
        
        return len(self.broken_links) == 0
    
    def generate_report(self, output_file='broken_links_report.md'):
        """Generate a markdown report of broken links."""
        if not self.broken_links:
            print("No broken links found! ✅")
            return
        
        report_content = f"""# Broken Links Report

Generated on: {datetime.now().strftime('%Y-%m-%d %H:%M:%S UTC')}

Found {len(self.broken_links)} broken link(s):

"""
        
        # Group by file
        files_with_broken_links = {}
        for link in self.broken_links:
            file_path = link['file']
            if file_path not in files_with_broken_links:
                files_with_broken_links[file_path] = []
            files_with_broken_links[file_path].append(link)
        
        for file_path, links in sorted(files_with_broken_links.items()):
            report_content += f"\n## File: `{file_path}`\n\n"
            for link in links:
                report_content += f"- **Line {link['line']}**: [{link['text']}]({link['url']})\n"
                report_content += f"  - URL: `{link['url']}`\n"
        
        report_content += f"\n---\n\n*Total broken links: {len(self.broken_links)}*\n"
        
        with open(output_file, 'w', encoding='utf-8') as f:
            f.write(report_content)
        
        print(f"Report saved to: {output_file}")

def main():
    """Main function to run the link checker."""
    checker = LinkChecker()
    
    print("🔗 Microsoft Build 2025 Repository Link Checker")
    print("=" * 50)
    
    success = checker.check_all_links()
    checker.generate_report()
    
    if not success:
        print("\n❌ Link checking failed - broken links found")
        sys.exit(1)
    else:
        print("\n✅ All links are working!")
        sys.exit(0)

if __name__ == '__main__':
    main()