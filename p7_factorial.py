
num = int(input("Enter the number:"))

fact = 1

# Calculate factorial using a for loop
for i in range(1, num + 1):
    fact *= i

print(f"The factorial of {num} is: {fact}")
