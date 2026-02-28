#!/bin/bash
# sync-v8dev.sh - Sync blog posts from v8.dev to reference folder

set -e

SCRIPT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
REFERENCE_DIR="$SCRIPT_DIR/../skills/reference"
V8DEV_DIR="$REFERENCE_DIR/v8.dev/src/blog"

echo "Syncing blog posts from v8.dev..."

# Check if v8.dev exists
if [ ! -d "$V8DEV_DIR" ]; then
    echo "Error: v8.dev not found. Please run: git submodule update --init"
    exit 1
fi

# Count files
total=$(ls -1 "$V8DEV_DIR"/*.md 2>/dev/null | wc -l)
echo "Found $total blog posts"

# Copy new/updated files
copied=0
for file in "$V8DEV_DIR"/*.md; do
    if [ -f "$file" ]; then
        filename=$(basename "$file")
        # Skip non-blog files
        if [[ "$filename" == "blog.json" ]]; then
            continue
        fi
        
        # Check if file is newer or doesn't exist in reference
        if [ ! -f "$REFERENCE_DIR/$filename" ] || [ "$file" -nt "$REFERENCE_DIR/$filename" ]; then
            cp -n "$file" "$REFERENCE_DIR/$filename"
            copied=$((copied + 1))
        fi
    fi
done

echo "Copied/updated $copied files"
echo "Done! Reference folder now has blog posts from v8.dev"
