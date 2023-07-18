# Check if the number sequences are the same
def check_spacing(number_sequence):
    first_sequence, second_sequence = get_number_sequences(number_sequence)
    assert first_sequence == second_sequence, "Error: Number sequences should be the same"

    return True


# Get the first and second number sequences
def get_number_sequences(number_sequence):
    first_sequence = ""
    second_sequence = ""
    is_first_sequence = True

# char.isdigit is for checking if the character, in this case number or letter is a number digit. 
# If so, it keeps track of it, and makes it part of the first sequence.
# The code continues until it hits a letter, ending the sequence, filtering through more numbers.
# Once it finds the second set of numbers, it records all, and checks to make sure they are the same as the first.

    for char in number_sequence:
        if char.isdigit():
            if is_first_sequence:
                first_sequence += char
            else:
                second_sequence += char
        else:
            is_first_sequence = False

    return first_sequence, second_sequence


# Testing the code with different scenarios
try:
    assert check_spacing("753159sajfkajfkjs753159")  # First scenario: Valid sequence
except AssertionError:
    print("Scenario 1 failed: Invalid sequence")

try:
    assert check_spacing("12345icancountfromonetofive12345")  # Second scenario: Valid sequence
except AssertionError:
    print("Scenario 2 failed: Invalid sequence")

try:
    assert check_spacing("852147sfasdfadfs852147")  # Third scenario: Valid sequence
except AssertionError:
    print("Scenario 3 failed: Invalid sequence")

print("This works")
