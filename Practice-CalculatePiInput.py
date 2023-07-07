# Set up variables to calculate
def calculate_pi(n):
    pi = 0.0
    sign = 1

    # Repeat the equation to find answer
    for i in range(n):
        term = sign * (1 / (2*i + 1))  # Calculate the current term of the series
        pi += term  # Add the term to the total sum
        sign *= -1  # Alternate the sign for the next term

    pi *= 4  # Multiply the sum by 4 to approximate pi
    return pi

num_terms = 100000  # Number of terms to be used for the approximation
exact_pi = calculate_pi(num_terms)  # Call the calculate_pi function to get the approximate value of pi
print("Exact value of pi:", exact_pi)  # Print the approximate value of pi

