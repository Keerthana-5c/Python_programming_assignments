import os
import shutil

# Specify the source directory where the unorganized files are located
source_directory = "/path/to/source/directory"

# Create a function to organize files by extension
def organize_files_by_extension(source_dir):
    # Iterate through all items (both files and directories) in the source directory
    for item in os.listdir(source_dir):
        item_path = os.path.join(source_dir, item)

        # Check if it's a file
        if os.path.isfile(item_path):
            # Get the file extension
            _, file_extension = os.path.splitext(item)

            # Create a subdirectory with the same name as the extension (excluding the dot)
            destination_dir = os.path.join(source_dir, file_extension[1:])

            # If the subdirectory doesn't exist, create it
            if not os.path.exists(destination_dir):
                os.makedirs(destination_dir)

            # Move the file to the corresponding subdirectory
            shutil.move(item_path, os.path.join(destination_dir, item))

# Call the function to organize the files
organize_files_by_extension(source_directory)
