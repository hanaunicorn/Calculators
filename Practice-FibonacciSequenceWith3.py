def dojob(n):
    # If n is 0 or negative, return 0
    if n <= 0:
        return 0
    # If n is 1, 2, or 3, return 1
    elif n <= 3:
        return 1

    # Initialize the first three numbers of the sequence to 1
    a, b, c = 1, 1, 1

    # Calculate the nth number of the sequence by adding the three previous numbers iteratively
    # Start from 4 as the first three numbers are already initialized
    for _ in range(4, n + 1):
        # Update the values of a, b, and c by shifting them to the right
        # a becomes the previous b, b becomes the previous c, and c is updated to the sum of the three
        a, b, c = b, c, a + b + c

    # The variable c holds the value of the nth number in the sequence
    return c

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
