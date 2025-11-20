#!/bin/bash

mkdir -p fire-downloads
cd fire-downloads

curl -s "https://firebasestorage.googleapis.com/v0/b/holidayhack2025.firebasestorage.app/o" \
  | jq -r '.items[].name' \
  | while read name; do
      encoded=$(python3 -c "import urllib.parse; print(urllib.parse.quote('''$name'''))")
      echo "Downloading: $name"
      curl -s -o "$(basename "$name")" \
        "https://firebasestorage.googleapis.com/v0/b/holidayhack2025.firebasestorage.app/o/$encoded?alt=media"
    done
