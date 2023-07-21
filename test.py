def sort_and_remove_duplicates(input_list):
    # Convert the elements to integers
    combined_list = [int(num) for num in input_list]

    # Remove duplicates by converting the combined list to a set and then sort it
    sorted_list = sorted(set(combined_list))
    return sorted_list

def dojob(input1, input2):
    # Ensure that the input lists contain only integers separated by spaces
    assert all(num.isdigit() for num in input1.split()), "list1 should contain only integers separated by spaces"
    assert all(num.isdigit() for num in input2.split()), "list2 should contain only integers separated by spaces"

    # Split the input strings into lists of integers
    input1_list = input1.split()
    input2_list = input2.split()

    combined_list = input1_list + input2_list
    sorted_list = sort_and_remove_duplicates(combined_list)

    # Assert the lists have no duplicates
    assert len(set(sorted_list)) == len(sorted_list), f"Combined list contains duplicates: {combined_list}"
    return sorted_list

def main():
    # Assert the sorted list is correct
    assert [1, 2, 3, 5, 6, 8] == dojob('1 1 1 2 2', '2 2 2 3 5 6 8')
    assert [1, 2] == dojob('1 1 1 2 2', '')
    assert [] == dojob('', '')

if __name__ == "__main__":
    main()
