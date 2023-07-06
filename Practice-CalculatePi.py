import math

def print_pi(digits):
    if digits <= 0:
        print("Number of digits must be positive.")
        return
    if digits > 50:
        print("The maximum number of digits is 50. Why do you need so many digits?")
        return
    precision = digits + 10
    pi = format(math.pi, f".{digits}f")
    print(f"Pi: {pi}")

# Example usage
tries = 3
for i in range(tries):
    digits = int(input("Enter the number of decimal digits of pi to print: "))
    if digits <= 50:
        print_pi(digits)
        print("Amazing. You understand how to follow instructions. 눈_눈")
        break
    elif i < tries - 1:
        print(f"The maximum number of digits is 50. Please comply if you want to use this. ლಠ益ಠლ)")
    else:
        print("I give up. ꒰╬•᷅д•᷄╬꒱")
