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
# "char.isdigit" is to determine if a character, in this case, the number that will repeat front and back is a number digit.
# Once it finishes the list of digits, it goes past all letters, that are tested, and continues on the second string of numbers
    for char in number_sequence:
        # Accumulate digits as part of the number sequences
        if char.isdigit():
            if is_first_sequence:
                first_sequence += char
            else:
                second_sequence += char
        else:
            # Once non-digit characters are encountered, switch to the second number sequence
            is_first_sequence = False

    return first_sequence, second_sequence


# Testing the code with different scenarios

if not check_spacing("753159sajfkajfkjs753159"):
    print("Scenario 1 failed: Invalid sequence")

if check_spacing("12345icancountfromonetofive12345"):
    print("Secnario 2 failed: Invalid sequence")
