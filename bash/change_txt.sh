#!/bin/bash

# Function to change file extensions to .txt
change_to_txt() {
    local dir="$1"
    
    # Change to the specified directory
    cd "$dir" || return
    
    # Process all files in current directory
    for file in *; do
        # Skip if it's not a file or directory
        [ -e "$file" ] || continue
        
        if [ -d "$file" ]; then
            # Recursively process subdirectories
            change_to_txt "$dir/$file"
        elif [ -f "$file" ]; then
            # Get the base name without extension
            filename=$(basename "$file")
            base="${filename%.*}"
            
            # Rename the file with .txt extension
            mv "$file" "$base.txt"
        fi
    done
    
    # Return to parent directory
    cd ..
}

# Start from the current directory
change_to_txt "$(pwd)"

echo "All files have been converted to .txt extension"