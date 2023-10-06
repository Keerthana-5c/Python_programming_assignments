import os
directory_path = "D:/python_practice/file_operations"
all_items = os.listdir(directory_path)# os.listdir() to get a list of all items in the directory

#list comprehension to filter out only the files (not directories)
files = [item for item in all_items if os.path.isfile(os.path.join(directory_path, item))]
file_count = len(files)
print(f"Number of files in the directory:",file_count)
