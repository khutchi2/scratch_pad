#!/bin/bash
# 1. List unique top-level entries in the tar
read -p "Input archive file name: " archive_name
tar -tf ${archive_name} | cut -d/ -f1 | sort -u > list.txt

# 2. Make your container
mkdir extracted

# 3. Move each one
while read dir; do
  # skip blank lines
  [ -z "$dir" ] && continue
  mv "$dir" extracted/ 2>/dev/null || echo "Skipping $dir (not found)"
done < list.txt
