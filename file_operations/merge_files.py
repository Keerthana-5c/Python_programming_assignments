with open('file1.txt','r') as fp: 
	data = fp.read()

with open('file2.txt','r') as fp:
	data2 = fp.read()


data = data +"\n"  #adds a newline character ("\n") to the end of the data string and assigns the result back to the variable data
data = data + data2 # this concatenates the data string with the contents of the data2 string and assigns the result back to the variable data.

with open ('file3.txt', 'w') as fp:
	fp.write(data)
