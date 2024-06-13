def factorial(n):
    """Calculate the factorial of a number."""
    if n == 0 or n == 1:
        return 1
    else:
        return n * factorial(n - 1)

# Input: Prompt the user to enter a number
number = int(input("Enter a number to calculate its factorial: "))

# Calculate and print the factorial using the function
result = factorial(number)
print(f"The factorial of {number} is: {result}")
