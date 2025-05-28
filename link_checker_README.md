# Link Checker Tools Documentation

This repository includes comprehensive tools for checking and fixing broken links in markdown files.

## Overview

The link checker implementation consists of:

1. **GitHub Actions Workflows** - Automated link checking
2. **Python Scripts** - Custom link checking and fixing tools
3. **Documentation** - Usage instructions and workflows

## GitHub Actions Workflows

### 1. Link Checker (`link-checker.yml`)

**Triggers:**
- Weekly schedule (Sundays at 2 AM UTC)
- Pull requests that modify markdown files
- Manual dispatch

**Features:**
- Uses custom Python script for comprehensive link checking
- Generates detailed broken links report
- Comments on PRs with broken link information
- Uploads reports as artifacts

### 2. Lychee Link Checker (`lychee-link-checker.yml`)

**Triggers:**
- Weekly schedule (Sundays at 3 AM UTC)
- Pull requests that modify markdown files
- Manual dispatch

**Features:**
- Uses the Lychee tool for fast link checking
- Creates GitHub issues for broken links
- Provides job summaries with detailed results

## Python Scripts

### 1. `link_checker.py` - Main Link Checker

A comprehensive Python script that scans all markdown files for URLs and tests their reachability.

**Usage:**
```bash
python3 link_checker.py
```

**Features:**
- Scans all `.md` files in the repository
- Extracts URLs from various markdown formats
- Tests HTTP/HTTPS links for reachability
- Generates detailed broken links report
- Includes retry logic and proper error handling
- Caches results to avoid duplicate checks

**Output:**
- Console output with real-time checking status
- `broken_links_report.md` file with detailed broken link information

### 2. `link_fixer.py` - Link Fixing Tool

A utility to help systematically fix broken links found by the checker.

**Usage:**

1. **Generate fixes template:**
   ```bash
   python3 link_fixer.py --template broken_links_report.md
   ```

2. **Apply fixes:**
   ```bash
   python3 link_fixer.py --fix
   ```

**Workflow:**
1. Run the link checker to generate `broken_links_report.md`
2. Generate a fixes template: `link_fixes.json`
3. Edit the JSON file to specify replacement URLs
4. Apply the fixes to update markdown files

## Usage Examples

### Basic Link Checking

```bash
# Run the link checker
python3 link_checker.py

# Check output
cat broken_links_report.md
```

### Fixing Broken Links

```bash
# 1. Generate fixes template from broken links report
python3 link_fixer.py --template broken_links_report.md

# 2. Edit link_fixes.json to specify new URLs
# Example link_fixes.json structure:
{
  "instructions": "Edit the 'new_url' field for each broken link...",
  "fixes": [
    {
      "file": "keynotes/KEY020/elements/github-copilot-automation.md",
      "line": 25,
      "text": "GitHub Copilot for Business",
      "old_url": "https://github.com/features/copilot/business",
      "new_url": "https://github.com/features/copilot/for-business"
    }
  ]
}

# 3. Apply the fixes
python3 link_fixer.py --fix
```

### GitHub Actions Integration

The workflows automatically:

1. **On Pull Requests:**
   - Check links in modified markdown files
   - Comment on PR if broken links are found
   - Upload detailed reports as artifacts

2. **Weekly Schedule:**
   - Comprehensive link checking across entire repository
   - Create issues for newly broken links
   - Maintain link health over time

## Configuration

### Link Checker Settings

You can modify `link_checker.py` to adjust:
- Request timeout (default: 10 seconds)
- Max retries (default: 2)
- User agent string
- URLs to skip or ignore

### Workflow Settings

Modify the workflow files (`.github/workflows/*.yml`) to adjust:
- Schedule timing
- Python version
- Action versions
- Trigger conditions

## Error Handling

The tools handle various scenarios:
- Network timeouts and connection errors
- HTTP error codes (4xx, 5xx)
- Malformed URLs
- Redirects and moved content
- Rate limiting

## Reporting

### Broken Links Report Format

The generated `broken_links_report.md` includes:
- Timestamp of check
- File-by-file breakdown of broken links
- Line numbers for each broken link
- Full URL information
- Summary statistics

### GitHub Integration

- **PR Comments:** Automatic comments on pull requests with broken links
- **Issues:** Automatic issue creation for broken links (Lychee workflow)
- **Artifacts:** Downloadable reports for detailed analysis

## Best Practices

1. **Regular Checks:** Use weekly scheduled runs to catch broken links early
2. **PR Integration:** Prevent new broken links from being merged
3. **Systematic Fixes:** Use the fixer tool for batch updates
4. **Documentation Updates:** Keep links current with content changes

## Troubleshooting

### Common Issues

1. **Rate Limiting:** Some sites may rate limit requests
   - Solution: Add delays or exclude problematic domains

2. **Firewall Blocks:** Corporate firewalls may block certain domains
   - Solution: Update firewall allow lists in GitHub settings

3. **Temporary Outages:** Sites may be temporarily unavailable
   - Solution: Re-run checks or verify manually

### Debug Mode

For troubleshooting, you can modify the scripts to:
- Increase verbosity
- Add debug logging
- Test specific URLs
- Adjust timeout values

## Contributing

When adding new markdown content:
1. Verify all links work before committing
2. Use HTTPS URLs when available
3. Prefer stable, canonical URLs
4. Test links in different browsers/contexts

The automated link checking will help maintain link quality over time.