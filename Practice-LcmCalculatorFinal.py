# Return true if a number is prime, otherwise false
def is_prime(n):
    if n <= 1:
        return False
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return False
    return True

# Generate a list of prime numbers up to a given limit
def generate_primes(limit):
    primes = []
    for number in range(2, limit + 1):
        if is_prime(number):
            primes.append(number)
    return primes

# Function to calculate prime factors of a number using the generated prime numbers list
def prime_factors(n):
    primes = generate_primes(n)
    factors = []
    for prime in primes:
        while n % prime == 0:
            factors.append(prime)
            n //= prime
        if n == 1:
            break
    if n > 1:
        factors.append(n)
    return factors

# Function to calculate the least common multiple (LCM) of two numbers
def calculate_lcm(a, b):
    prime_factors_a = prime_factors(a)
    prime_factors_b = prime_factors(b)
    all_factors = prime_factors_a + prime_factors_b

    unique_factors = []
    lcm = 1
    for factor in all_factors:
        if factor not in unique_factors:
            unique_factors.append(factor)
            lcm *= factor ** max(prime_factors_a.count(factor), prime_factors_b.count(factor))

    return lcm

# Prompt user to input two positive whole numbers separated by commas
numbers_input = input("Enter two positive whole numbers separated by commas to find the LCM: ")
numbers_list = numbers_input.split(",")

# Extract and convert the input numbers
number_one = int(numbers_list[0].strip())
number_two = int(numbers_list[1].strip())

# Calculate prime factors for each input number
prime_factors_one = prime_factors(number_one)
prime_factors_two = prime_factors(number_two)

# Print the input numbers and their respective prime factors
print("For", number_one, ", these are all prime factors:", prime_factors_one)
print("For", number_two, ", these are all prime factors:", prime_factors_two)

# Calculate the least common multiple (LCM) of the input numbers
lcm = calculate_lcm(number_one, number_two)

# Print the least common multiple (LCM)
print("The LCM of", number_one, "and", number_two, "is:", lcm)
