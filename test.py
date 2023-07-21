def dojob(input1, input2):
    # Convert the elements to integers and split the input strings into lists of integers
    input1_list = list(map(int, input1.split()))
    input2_list = list(map(int, input2.split()))

    # Initialize variables to keep track of the current indices for both lists
    x, y = 0, 0
    result = []

    # Compare elements from both lists and add them to the result list accordingly
    while x < len(input1_list) and y < len(input2_list):
        if input1_list[x] <= input2_list[y]:
            result.append(input1_list[x])
            x += 1
        else:
            result.append(input2_list[y])
            y += 1

    # Add any remaining elements from the first list
    result.extend(input1_list[x:])

    # Add any remaining elements from the second list
    result.extend(input2_list[y:])

    return result

def main():
    # Assert the sorted list is correct
    assert [1, 2, 3, 5, 8] == dojob('1 1 3 5', '2 4 8')
    assert [1, 2] == dojob('1 1 1 2 2', '')
    assert [] == dojob('', '')

if __name__ == "__main__":
    main()
