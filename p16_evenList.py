# Step 1: Input
original_list = input("Enter elements of the list separated by spaces: ").split()

# Step 2: Filter Odd Numbers
filtered_list = [int(num) for num in original_list if int(num) % 2 != 0]

# Step 3: Print Result
print("Original List:", original_list)
print("Filtered List (without even numbers):", filtered_list)
