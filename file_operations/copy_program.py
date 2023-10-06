
file1 = open("file1.txt","r") #open one file that contains text in read mode
file2 = open("file2.txt","a")# open another file in append mode
for text in file1:
    file2.write(text)   #writes the text in file1 to file 2

# import shutil      
# file1 = 'D:/python_practice/file1.txt'
# file2 = 'D:/python_practice/file2.txt'
# shutil.copyfile(file1,file2)    #copies the content from source file to destination file