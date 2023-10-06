import os
for data in os.listdir("D:/python_practice/file_operations"):# gives the list of files present in the directory
    if data.endswith(".py"):      #checks for the files inside the data list endswith given file extension
        print(data)