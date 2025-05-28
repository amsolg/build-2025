#!/usr/bin/env python3

import re
import os
import json
import argparse
from pathlib import Path

def load_broken_links():
    """Load the broken links from the report file"""
    try:
        with open('broken_links_fixes.json', 'r', encoding='utf-8') as f:
            return json.load(f)
    except FileNotFoundError:
        print("Error: broken_links_fixes.json file not found.")
        return {}

def fix_broken_links(fixes_data):
    """Fix broken links in files based on the provided fixes data"""
    if not fixes_data:
        print("No fixes specified.")
        return
    
    base_path = os.path.dirname(os.path.abspath(__file__))
    
    for file_path, links in fixes_data.items():
        full_path = os.path.join(base_path, file_path)
        
        try:
            with open(full_path, 'r', encoding='utf-8') as f:
                content = f.read()
            
            # Make the replacements
            updated_content = content
            for old_url, new_url in links.items():
                if new_url:  # Only replace if a new URL is provided
                    # Escape special characters in the old URL for regex
                    escaped_old_url = re.escape(old_url)
                    updated_content = re.sub(
                        f"({escaped_old_url})", 
                        new_url, 
                        updated_content
                    )
            
            # Write the updated content back to the file
            if updated_content != content:
                with open(full_path, 'w', encoding='utf-8') as f:
                    f.write(updated_content)
                print(f"Fixed links in {file_path}")
            else:
                print(f"No changes made to {file_path}")
                
        except Exception as e:
            print(f"Error processing {file_path}: {str(e)}")

def generate_fixes_template(report_file):
    """Generate a template JSON file for specifying fixes"""
    try:
        with open(report_file, 'r', encoding='utf-8') as f:
            report = f.read()
        
        # Extract broken links from the report
        fixes = {}
        current_file = None
        
        for line in report.split('\n'):
            if line.startswith('## '):
                current_file = line[3:].strip()
                fixes[current_file] = {}
            elif line.startswith('- Line ') and current_file:
                url_match = re.search(r'\[(.*?)\]', line)
                if url_match:
                    url = url_match.group(1)
                    fixes[current_file][url] = ""
        
        # Write the template to a JSON file
        with open('broken_links_fixes.json', 'w', encoding='utf-8') as f:
            json.dump(fixes, f, indent=2)
        
        print("Template JSON file for fixes generated: broken_links_fixes.json")
        print("Edit this file to specify the replacement URLs, then run this script again with --fix.")
        
    except Exception as e:
        print(f"Error generating template: {str(e)}")

def main():
    parser = argparse.ArgumentParser(description="Fix broken links in markdown files")
    parser.add_argument('--template', dest='report_file', help='Generate a template JSON from the report file')
    parser.add_argument('--fix', action='store_true', help='Fix broken links using the broken_links_fixes.json file')
    
    args = parser.parse_args()
    
    if args.report_file:
        generate_fixes_template(args.report_file)
    elif args.fix:
        fixes_data = load_broken_links()
        fix_broken_links(fixes_data)
    else:
        parser.print_help()

if __name__ == "__main__":
    main()