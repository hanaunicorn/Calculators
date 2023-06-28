# Input five numbers separated by commas
numbers_input = input("Enter five positive whole numbers separated by commas: ")
numbers_list = numbers_input.split(",")

# Input the minimum total
minimum_total = int(input("Enter the minimum total: "))

# Find pairs of numbers that add up to be larger than the minimum total
pairs = []
for i in range(len(numbers_list)):
    for j in range(i + 1, len(numbers_list)):
        if int(numbers_list[i]) + int(numbers_list[j]) > minimum_total:
            pairs.append((numbers_list[i], numbers_list[j]))

# Print the pairs of numbers
if pairs:
    print("Pairs of numbers that add up to be larger than the minimum total:")
    for pair in pairs:
        print(pair[0], pair[1], sep=', ')
else:
    print("No pairs found")
