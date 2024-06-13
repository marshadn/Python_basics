# Prompt the user to enter a string
input_str = input("Enter a string: ")

# Check if the length of the input string is greater than 1
if len(input_str) > 1:
    # Exchange the first and last characters using string slicing
    modified_string = input_str[-1] + input_str[1:-1] + input_str[0]
    print("Modified String:", modified_string)
else:
    # If the string has one or zero characters, no exchange is possible
    print("No modification needed. Original String:", input_str)
