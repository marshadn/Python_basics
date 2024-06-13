def print_pattern(num_rows):
    """Print the given pattern using nested loops."""
   # Upper part of the pattern
   
    for i in range(1, num_rows + 1):
        print('*' * i)

    # Lower part of the pattern
    for i in range(num_rows - 1, 0, -1):
        print('*' * i)

# Input: Prompt the user to enter the number of rows
num_rows = int(input("Enter the number of rows for the pattern: "))

# Call the function to print the pattern
print_pattern(num_rows)




















