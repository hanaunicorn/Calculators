def bubble_sort(numbers):
    n = len(numbers)
    for b in range(n): # Sets the range of numbers
        for c in range(0, n - b - 1): #  Ensures there are no duplicates of a number
            if numbers[c] > numbers[c + 1]: # Sorts the numbers by comparing and switching the positions of numbers
                numbers[c], numbers[c + 1] = numbers[c + 1], numbers[c]

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
