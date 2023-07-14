def find_smallest(input_list): # Replaces idx to find smallest number
    smallest = input_list[0] # Clean list to input more number into later
    for num in input_list:
        if num < smallest: # Starts with 1st number, tries to find something smaller
            smallest = num
    return smallest

def selection_sort(input_list):
    sorted_list = []
    while input_list:
        smallest = find_smallest(input_list)
        sorted_list.append(smallest) # Builds up the list by adding "smallest" numbers 
        input_list.remove(smallest) # Removes the output list numbers repeat from the Input list
    return sorted_list

input_str = input("Enter a list of numbers separated by spaces: ") # Asks user to input numbers

try: # Prints out the output
    input_list = list(map(int, input_str.split()))
    sorted_list = selection_sort(input_list)
    print("Sorted list:", sorted_list)
    
except ValueError: # Error Message
    print("Invalid input. Please enter a valid list of numbers separated by spaces.")
