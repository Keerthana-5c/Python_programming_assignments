with open("file.txt", "r") as myfile:  #open the file in read mode
   data = myfile.read()                 #read the content inside the file and store it inside the data
rev_data = data[::-1]                 # Reversing the data by passing -1 for [start: end: step]
print(rev_data)