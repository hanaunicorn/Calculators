def sort_and_remove_duplicates(input_list):
    # Combine the two lists
    combined_list = input_list.split()

    # Convert the elements to integers
    combined_list = [int(num) for num in combined_list]

    # Remove duplicates by converting the combined list to a set and then sort it
    sorted_list = sorted(set(combined_list))
    return sorted_list

def main():
    # Input the two lists directly using assert with proper format
    list1 = "1 1 3 5"  # Modify the values in the list1 and list2 strings as needed
    list2 = "2 6 8"

    # Ensure that the input lists contain only integers separated by spaces
    assert all(num.isdigit() for num in list1.split()), "list1 should contain only integers separated by spaces"
    assert all(num.isdigit() for num in list2.split()), "list2 should contain only integers separated by spaces"

    # Combine the two lists and remove duplicates
    combined_list = list1.split() + list2.split()
    sorted_list = sort_and_remove_duplicates(' '.join(combined_list))

    # Print the sorted result with duplicates removed
    print("Sorted result in ascending order (with duplicates removed):")
    print(*sorted_list)

    # Assert the lists have no duplicates
    assert len(set(sorted_list)) == len(sorted_list), f"Combined list contains duplicates: {combined_list}"

    # Assert the sorted list is correct
    assert sorted_list == [1, 2, 3, 5, 6, 8], f"Sorting failed. Expected: [1, 2, 3, 5, 6, 8], Got: {sorted_list}"

if __name__ == "__main__":
    main()
