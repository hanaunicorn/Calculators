def dojob(n):
    # Base cases: n <= 0 returns 0, n <= 3 returns 1
    if n <= 0:
        return 0
    elif n <= 3:
        return 1

    # Recursive step: Calculate the nth number by summing the results of the three previous numbers
    return dojob(n - 1) + dojob(n - 2) + dojob(n - 3)

# Get user input for the value of n
n = None

# Use a while loop to ensure the user enters a valid integer for n
while n is None:
    # Prompt the user to enter a value for n
    user_input = input("Enter the value of n: ")
    
    # Check if the user input is a valid integer (made of digits only)
    if user_input.isdigit():
        # Convert the user input to an integer and assign it to n
        n = int(user_input)
    else:
        # If the input is not a valid integer, display an error message
        print("Invalid input. Please enter an integer for n.")

# Call the dojob function with the user input value of n and store the result
result = dojob(n)

# Print the nth number in the sequence
print(f"The {n}th number in the sequence is: {result}")
