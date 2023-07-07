# Set up variables to calculate
def calculate_pi(n):
    pi = 3.0
    sign = 1

    # Repeat the equation to find the answer
    for i in range(1, n+1):
        term = sign * (4 / ((2*i) * (2*i+1) * (2*i+2)))  # Calculate the current term of the series
        pi += term  # Add the term to the total sum
        sign *= -1  # Alternate the sign for the next term

    return pi

num_terms = 100000  # Number of terms to be used for the approximation
approximate_pi = calculate_pi(num_terms)  # Call the calculate_pi_nilakantha function
print("Approximate value of pi using Nilakantha series:", approximate_pi)  # Print the approximate value of pi
