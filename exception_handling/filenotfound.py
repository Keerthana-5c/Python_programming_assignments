try:
    # Attempt to open a file that may or may not exist
    file_path = "D:/python_practice/exception_handling/notfile1.txt"
    with open(file_path, "r") as file:
        content = file.read()
    print("File content:", content)

# except FileNotFoundError:
#     # Handle the "File Not Found" error here
#     print("The file was not found.")

except Exception as e:
    # Handle other exceptions, if necessary
    print(f"An error occurred: {e}")
