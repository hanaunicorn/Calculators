def isprimefn(b):
    isprime = True
    for a in range(2, b):
        if b % a == 0:
            isprime = False
            break
    return isprime

print("These are all the prime numbers from 1 through 1000 that contain the digit 9:")

for a in range(1000):
    if isprimefn(a):
        if a > 1 and '9' in str(a):  # Add condition to check if '9' is in the number
            print(a)
