# Link Checker Tools

This directory contains tools for checking and fixing broken links in markdown files within the repository.

## Tools

### 1. `link_checker.py`

This script scans all markdown files in the repository for URLs and checks if they are reachable.

**Usage:**
```bash
python3 link_checker.py
```

**Features:**
- Finds all markdown files in the repository
- Extracts URLs from markdown files
- Checks if URLs are reachable
- Generates a report of broken links

### 2. `link_fixer.py`

This script helps fix broken links identified by the link checker.

**Usage:**

1. Generate a template JSON file from the report:
```bash
python3 link_fixer.py --template broken_links_report.md
```

2. Edit the generated `broken_links_fixes.json` file to specify replacements for broken links.
   - For each broken link, provide a replacement URL or leave it as an empty string to skip.

3. Fix the broken links using the edited JSON file:
```bash
python3 link_fixer.py --fix
```

## Workflow

1. Run the link checker to identify broken links:
```bash
python3 link_checker.py
```

2. Review the generated `broken_links_report.md` file to see the list of broken links.

3. Generate a template for fixing broken links:
```bash
python3 link_fixer.py --template broken_links_report.md
```

4. Edit the `broken_links_fixes.json` file to provide replacements for broken links.

5. Fix the broken links using the edited JSON file:
```bash
python3 link_fixer.py --fix
```

6. Run the link checker again to verify that the links have been fixed:
```bash
python3 link_checker.py
```

## Example

Suppose the link checker found a broken link to `https://old-url.com` in a markdown file. The JSON file would look like:

```json
{
  "path/to/file.md": {
    "https://old-url.com": ""
  }
}
```

To fix it, edit the JSON file to provide a replacement URL:

```json
{
  "path/to/file.md": {
    "https://old-url.com": "https://new-url.com"
  }
}
```

Then run `python3 link_fixer.py --fix` to apply the changes.