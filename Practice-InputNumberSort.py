def bubble_sort(numbers):
    n = len(numbers)
    for i in range(n):
        for j in range(0, n - i - 1):
            if numbers[j] > numbers[j + 1]:
                numbers[j], numbers[j + 1] = numbers[j + 1], numbers[j]

numbers_input = input("Enter numbers separated by commas: ")

# Split the input string into a list of numbers
numbers = [int(num) for num in numbers_input.split(',')]

order = input("Choose the order (a - ascending, b - descending): ")

if order.lower() == 'a':
    # Sort the numbers in ascending order using bubble sort
    bubble_sort(numbers)
elif order.lower() == 'b':
    # Sort the numbers in descending order using bubble sort
    bubble_sort(numbers)
    numbers.reverse()
else:
    print("Invalid choice. Defaulting to ascending order.")
    bubble_sort(numbers)
