import os
directory_path = "D:/python_practice/file_operations"
files = os.listdir(directory_path)  # List all files in the directory
empty_files = []

for filename in files:
    file_path = os.path.join(directory_path, filename)  #creates the full path of the file
    if os.path.isfile(file_path) and os.path.getsize(file_path) == 0:  #checks for the size of the file
        empty_files.append(filename)    #if the file size is zero append the file name to the empty file list

print("Empty files in the given directory:")
for empty_file in empty_files:
    print(empty_file)
