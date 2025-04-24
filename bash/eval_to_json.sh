#!/usr/bin/env bash
set -euo pipefail

LOG_DIR="logs"
JSON_DIR="json_logs"

# Create the target directory if it doesn't exist
mkdir -p "${JSON_DIR}"

# Loop over every file in logs/
for filepath in "${LOG_DIR}"/*; do
  # Skip if not a regular file
  [ -f "$filepath" ] || continue

  # Extract the base name and change extension to .json
  filename=$(basename "$filepath")
  name="${filename%.*}"
  output="${JSON_DIR}/${name}.json"

  # === INSERT YOUR CONVERSION COMMAND BELOW ===
  # e.g. convert_to_json "$filepath" > "$output"
  inspect log dump "$filepath" > "$output"
  # ============================================

  echo "Converted: $filepath → $output"
done
