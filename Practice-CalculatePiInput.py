import math

def calculate_pi(digits):
    if digits <= 0:
        print("Number of digits must be positive.")
        return

    # Set the precision for pi calculation
    precision = digits + 2

    # Calculate pi with the desired number of digits
    pi = str(round(math.pi, precision))

    # Print the calculated value of pi
    print(f"Pi: {pi}")


def calculate_circle():
    circumference = float(input("Enter the circumference of the circle: "))
    diameter = float(input("Enter the diameter of the circle: "))

    # Calculate radius using the given diameter
    radius = diameter / 2

    # Check if diameter and circumference form a valid circle
    if circumference <= 0 or diameter <= 0 or abs(circumference - math.pi * diameter) > 1e-6:
        print("Invalid circle.")
        return

    # Print the calculated radius
    print(f"Radius: {radius}")


# Example usage
calculate_circle()

digits = int(input("Enter the number of digits for pi calculation: "))
calculate_pi(digits)
