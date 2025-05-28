#!/bin/bash

# Install lychee if not already installed
if ! command -v lychee &> /dev/null
then
    echo "Installing lychee..."
    cargo install lychee
fi

# Create output directory
mkdir -p reports

# Run lychee on all markdown files
echo "Checking links in markdown files..."
find . -name "*.md" | xargs lychee --verbose --no-progress --format markdown --output ./reports/lychee_broken_links.md

echo "Link check completed. Results saved to ./reports/lychee_broken_links.md"