def print_pi(digits):
    predetermined_pi = "3.14159265358979323846264338327950288419716939937510"
    if digits <= 0:
        print("Number of digits must be positive.")
        return
    if digits > 50:
        print("The maximum number of digits is 50. Why do you need so many digits?")
        return
    pi = predetermined_pi[:digits+2]  # Add 2 to include the leading '3.' in the predetermined value
    print(f"Pi: {pi}")

# Example usage
tries = 3
for i in range(tries):
    digits = int(input("Enter the number of decimal digits of pi to print: "))
    if digits <= 50:
        print_pi(digits)
        if i == 0:
            print("You are a certified smart person.")
        print("You understand how to follow instructions. 눈_눈")
        break
    elif i < tries - 1:
        print("The maximum number of digits is 50. Please comply if you want to use this. ლಠ益ಠლ)")
    else:
        print("I give up. ꒰╬•᷅д•᷄╬꒱")

