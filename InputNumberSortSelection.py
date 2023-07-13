# Selection sort version of InputNumberSort.py
def selection_sort(input_list):
    for a in range(len(input_list)):
        min_idx = idx
        for j in range(idx + 1, len(input_list)):
            if input_list[min_idx] > input_list[j]:
                min_idx = j
        # Swap the minimum value with the compared value
        input_list[idx], input_list[min_idx] = input_list[min_idx], input_list[idx]
'''
Index isolates the smallest number, which is how Selection Sort works.
It then stacks and sorts more numbers following it.
'''
input_str = input("Enter a list of numbers separated by spaces: ")

try: # Finalizes list, and prints
    input_list = list(map(int, input_str.split()))
    selection_sort(input_list)
    print("Sorted list:", input_list)
except ValueError: # Error Message
    print("Invalid input. Please enter a valid list of numbers separated by spaces.")

