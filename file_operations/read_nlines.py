file = open('file3.txt')
data = file.readlines() #readlines() returns a list containing each line in the file as a list
n = int(input("Enter the number of lines need to print:"))
print(data[:n])    #prints the items inside the data from 0 th index to nth index
