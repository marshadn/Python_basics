# Prompt the user to enter two strings
string1 = input("Enter the first string: ")
string2 = input("Enter the second string: ")

# Check if both strings have at least 2 characters
if len(string1) >= 2 and len(string2) >= 2:
    # Swap characters at position 1 in each string
    modified_string1 = string2[0] + string1[1:]  # First character from string2 and rest from string1
    modified_string2 = string1[0] + string2[1:]  # First character from string1 and rest from string2

    # Concatenate the modified strings with a space in between
    result_string = modified_string1 + ' ' + modified_string2

    # Print the result
    print("Modified String:", result_string)
else:
    # Print an error message if either string is too short
    print("Both strings should have at least 2 characters for swapping.")
