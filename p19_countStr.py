def count_characters(input_string):
    """Count the number of characters in a string."""
    char_count = {}

    for char in input_string:
        if char in char_count:
            char_count[char] += 1
        else:
            char_count[char] = 1

    return char_count

# Input: Prompt the user to enter a string
user_string = input("Enter a string: ")

# Call the function to count characters
result = count_characters(user_string)

# Print the character count
print("Character Count:")
for char, count in result.items():
    print(f"'{char}': {count}")
