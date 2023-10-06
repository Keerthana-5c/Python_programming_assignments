try:
    # Prompt the user for an integer input
    user_input = int(input("Enter an integer: "))
    print("You entered:", user_input)

except ValueError:
    # Handle the ValueError (e.g., non-integer input)
    print("Invalid input. Please enter a valid integer.")

except Exception as e:
    # Handle other exceptions, if necessary
    print(f"An error occurred: {e}")
