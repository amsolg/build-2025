#!/usr/bin/env python3
"""
Link Fixer for Microsoft Build 2025 Repository

This script helps fix broken links by generating a template JSON file from the
broken links report and applying fixes based on the edited JSON file.
"""

import json
import re
import argparse
from pathlib import Path
import sys

class LinkFixer:
    def __init__(self, root_dir='.'):
        self.root_dir = Path(root_dir)
        self.fixes_file = 'link_fixes.json'
        
    def parse_broken_links_report(self, report_file='broken_links_report.md'):
        """Parse the broken links report and extract link information."""
        if not Path(report_file).exists():
            print(f"Error: {report_file} not found")
            return []
        
        broken_links = []
        current_file = None
        
        with open(report_file, 'r', encoding='utf-8') as f:
            content = f.read()
        
        # Parse the markdown report
        lines = content.split('\n')
        for line in lines:
            # Look for file headers
            if line.startswith('## File: `') and line.endswith('`'):
                current_file = line[10:-1]  # Extract filename
            
            # Look for broken link entries
            elif line.startswith('- **Line ') and '**: ' in line:
                if current_file:
                    # Extract line number and URL
                    match = re.search(r'- \*\*Line (\d+)\*\*: \[([^\]]*)\]\(([^)]+)\)', line)
                    if match:
                        line_num = int(match.group(1))
                        link_text = match.group(2)
                        old_url = match.group(3)
                        
                        broken_links.append({
                            'file': current_file,
                            'line': line_num,
                            'text': link_text,
                            'old_url': old_url,
                            'new_url': ''  # To be filled by user
                        })
        
        return broken_links
    
    def generate_fixes_template(self, report_file='broken_links_report.md'):
        """Generate a JSON template file for fixing broken links."""
        broken_links = self.parse_broken_links_report(report_file)
        
        if not broken_links:
            print("No broken links found in report")
            return False
        
        # Create a structured template for fixes
        fixes_template = {
            "instructions": "Edit the 'new_url' field for each broken link. Leave empty to skip fixing that link.",
            "fixes": broken_links
        }
        
        with open(self.fixes_file, 'w', encoding='utf-8') as f:
            json.dump(fixes_template, f, indent=2, ensure_ascii=False)
        
        print(f"Generated fixes template: {self.fixes_file}")
        print(f"Found {len(broken_links)} broken links to fix")
        print(f"Edit {self.fixes_file} and set 'new_url' values, then run with --fix")
        
        return True
    
    def apply_fixes(self):
        """Apply the fixes from the JSON file to the actual markdown files."""
        if not Path(self.fixes_file).exists():
            print(f"Error: {self.fixes_file} not found. Run with --template first.")
            return False
        
        with open(self.fixes_file, 'r', encoding='utf-8') as f:
            fixes_data = json.load(f)
        
        fixes = fixes_data.get('fixes', [])
        applied_fixes = 0
        
        # Group fixes by file for efficient processing
        fixes_by_file = {}
        for fix in fixes:
            if fix['new_url']:  # Only process fixes with new URLs
                file_path = fix['file']
                if file_path not in fixes_by_file:
                    fixes_by_file[file_path] = []
                fixes_by_file[file_path].append(fix)
        
        for file_path, file_fixes in fixes_by_file.items():
            full_path = self.root_dir / file_path
            
            if not full_path.exists():
                print(f"Warning: File not found: {file_path}")
                continue
            
            # Read the file
            with open(full_path, 'r', encoding='utf-8') as f:
                lines = f.readlines()
            
            # Apply fixes (in reverse line order to maintain line numbers)
            file_fixes.sort(key=lambda x: x['line'], reverse=True)
            
            for fix in file_fixes:
                line_idx = fix['line'] - 1  # Convert to 0-based index
                
                if line_idx < len(lines):
                    old_line = lines[line_idx]
                    new_line = old_line.replace(fix['old_url'], fix['new_url'])
                    
                    if new_line != old_line:
                        lines[line_idx] = new_line
                        applied_fixes += 1
                        print(f"Fixed: {file_path}:{fix['line']} - {fix['old_url']} -> {fix['new_url']}")
                    else:
                        print(f"Warning: Could not find URL to replace in {file_path}:{fix['line']}")
            
            # Write the file back
            with open(full_path, 'w', encoding='utf-8') as f:
                f.writelines(lines)
        
        print(f"Applied {applied_fixes} fixes across {len(fixes_by_file)} files")
        return applied_fixes > 0

def main():
    """Main function for the link fixer."""
    parser = argparse.ArgumentParser(description='Fix broken links in markdown files')
    parser.add_argument('--template', metavar='REPORT_FILE', 
                       help='Generate fixes template from broken links report (default: broken_links_report.md)')
    parser.add_argument('--fix', action='store_true',
                       help='Apply fixes from link_fixes.json')
    parser.add_argument('--root', default='.',
                       help='Root directory of the repository (default: .)')
    
    args = parser.parse_args()
    
    if not args.template and not args.fix:
        parser.print_help()
        return
    
    fixer = LinkFixer(args.root)
    
    if args.template:
        report_file = args.template if args.template != 'broken_links_report.md' else 'broken_links_report.md'
        success = fixer.generate_fixes_template(report_file)
        sys.exit(0 if success else 1)
    
    elif args.fix:
        success = fixer.apply_fixes()
        sys.exit(0 if success else 1)

if __name__ == '__main__':
    main()