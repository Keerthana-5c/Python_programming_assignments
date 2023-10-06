count = 0
with open("file.txt", "r") as file: #open the file in read mode 
    data = file.read()    
    word_count = data.split()  #split()- splits the string into a list of substrings
    count = len(word_count)   #counting the number of strings inside the 'word_count' list 
print(count)
