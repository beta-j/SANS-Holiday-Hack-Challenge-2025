#!/bin/bash

BUCKET="holidayhack2025.firebasestorage.app"
API="https://firebasestorage.googleapis.com/v0/b/$BUCKET/o"

# Get file list again
curl -s "$API" | jq -r '.items[].name' > files.txt

while IFS= read -r name; do
    encoded=$(python3 - <<EOF
import urllib.parse
print(urllib.parse.quote("$name", safe=""))
EOF
)

    # Create target directory (handles gnome-avatars/, gnome-documents/)
    mkdir -p "fire-downloads/$(dirname "$name")"

    echo "Downloading $name ..."
    curl -s -o "fire-downloads/$name" "$API/$encoded?alt=media"
done < files.txt
