#!/bin/bash

# Usage:
#   ./leetcode.sh --generate <leetcode-url>
#   ./leetcode.sh --update <folder-name>

PYTHON_SCRIPT="leetcode-scrape.py"

# Check for Python script existence
if [ ! -f "$PYTHON_SCRIPT" ]; then
    echo "❌ Error: $PYTHON_SCRIPT not found in current directory."
    exit 1
fi

# Parse arguments
if [ "$1" == "--generate" ]; then
    if [ -z "$2" ]; then
        echo "❌ Error: Please provide a LeetCode URL."
        exit 1
    fi

    # Run generate command and capture frontend ID from output
    output=$(python3 "$PYTHON_SCRIPT" generate "$2")
    echo "$output" || exit 1

elif [ "$1" == "--update" ]; then
    if [ -z "$2" ]; then
        echo "❌ Error: Please provide a folder name to update."
        exit 1
    fi

    if [ ! -d "$2" ]; then
        echo "❌ Error: Folder '$2' does not exist."
        exit 1
    fi

    python3 "$PYTHON_SCRIPT" update "$2"

else
    echo "❌ Invalid usage."
    echo "Usage:"
    echo "  $0 --generate <leetcode-url>"
    echo "  $0 --update <folder-name>"
    exit 1
fi
