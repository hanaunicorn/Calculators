def sort_and_remove_duplicates(input_list):
    # Combine the two lists
    combined_list = input_list.split()

    # Convert the elements to integers
    combined_list = [int(num) for num in combined_list]

    # Remove duplicates by converting the combined list to a set and then sort it
    sorted_list = sorted(set(combined_list))
    return sorted_list

def main():
    # Input the two lists directly using assert
    assert (list1 := "1 1 3 5")  # Modify the values in the list1 and list2 strings as needed
    assert (list2 := "2 6 8")

    # Combine the two lists and remove duplicates
    combined_list = list1.split() + list2.split()
    sorted_list = sort_and_remove_duplicates(' '.join(combined_list))

    # Print the sorted result with duplicates removed
    print("Sorted result in ascending order (with duplicates removed):")
    print(*sorted_list)

    # Assert the lists have no duplicates
    assert len(set(sorted_list)) == len(sorted_list), f"Combined list contains duplicates: {combined_list}"

    # Assert the sorted list is correct
    expected_result = sorted(list(set(sorted_list)))
    assert sorted_list == expected_result, f"Sorting failed. Expected: {expected_result}, Got: {sorted_list}"

if __name__ == "__main__":
    main()