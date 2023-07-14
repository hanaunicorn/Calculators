def add_numbers(num1, num2):
    if len(num1) > 100 or len(num2) > 100:
        return "Error: Numbers exceed maximum length of 100 digits."

   # Adds "0" for place holder in front of numbers so that the amount of digits are the same
    if len(num1) < len(num2): 
        num1 = num1.zfill(len(num2))
        
    else: # 
        num2 = num2.zfill(len(num1))
    result = ""
    carry = 0

    # Calculate
    assert len(num1) == len(num2)
    for i in range(len(num1) - 1, -1, -1):
        digit_sum = int(num1[i]) + int(num2[i]) + carry
        digit = digit_sum % 10
        carry = digit_sum // 10
        result = str(digit) + result

    if carry:
        result = str(carry) + result

    return result

# Test the function
assert(add_numbers("2", "8")=="10");
assert(add_numbers("2", "888")=="890");
assert(add_numbers("1", "2")=="3");
assert(add_numbers("19999999999", "1")=="20000000000");
assert(add_numbers("1111111111111111111111111111111", "2")=="1111111111111111111111111111113");
numbers = input("Enter two numbers: ").split()
result = add_numbers(numbers[0], numbers[1])
print("Sum:", result)
