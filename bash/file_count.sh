#!/bin/bash
# file_count.sh
#!/usr/bin/env bash
read -p "Input directory to go through: " directory

# make sure it even exists
if [[ ! -d "$directory" ]]; then
  echo "Error: '$directory' is not a directory." >&2
  exit 1
fi

# iterate over each entry inside $directory
for dir in "$directory"/*; do
  # only process subdirectories
  if [[ -d "$dir" ]]; then
    # count only the files (not counting subdirectories)
    num_files=$(find "$dir" -maxdepth 1 -type f | wc -l)
    echo "Folder: $dir — Number of files: $num_files"
  fi
done

