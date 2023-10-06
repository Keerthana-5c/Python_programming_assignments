try:
    num1 = int(input("Enter a number: "))
    num2 = int(input("Enter another number: "))
    result = num1 / num2

except ValueError:           #handles value error
    print("Invalid input. Please enter valid integers.")

except ZeroDivisionError:       #handles zerodivision error
    print("Cannot divide by zero.")

except Exception as e:           #handle other exceptions
    print(f"An error occurred: {e}")

else:                            #executes when there is no error
    print(f"The result of the division is: {result}")
