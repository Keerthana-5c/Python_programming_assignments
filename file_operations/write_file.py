
with open("user_input.txt", "w") as file: #opens the file in read mode 
    while True:            
        user_input = input("Enter text: ")  # getting input from the user
        if user_input.lower() == 'exit':    #terminate the loop if the user input has 'exit' word
            break  
        file.write(user_input + '\n')   #writes the input text in a file with newline character
print("Written")
