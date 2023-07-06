import math

def calculate_pi(circumference, diameter):
    pi = circumference / diameter
    pi = round(pi, 13)  # Round the value of pi to 13 decimal places
    return pi

# Get user input
circumference = float(input("Enter the circumference: "))
diameter = float(input("Enter the diameter: "))

# Calculate pi
pi = calculate_pi(circumference, diameter)

# Format the string without trailing zeros
pi_str = format(pi, '.13f').rstrip('0')

# Print the first 13 digits of pi
print(f"The first 13 digits of pi (the last digit is rounded) are: {pi_str}")
