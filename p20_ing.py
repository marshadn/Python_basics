def my_string(input_string):
    """Add 'ly' to the end of a string, or 'ing' if it already ends with 'ing'."""
    if input_string.endswith('ing'):
        return input_string + 'ly'
    else:
        return input_string + 'ing'

# Input: Prompt the user to enter a string
str = input("Enter a string: ")

# Call the function to add 'ly' or 'ing' to the string
result = my_string(str)

# Print the result
print("Modified String:", result)
