a=int(input("Enter the 1st no:"))
b=int(input("Enter the 2nd no:"))
print(f"Before swapping a={a} and b={b}")
a=a+b
b=a-b
a=a-b
print(f"After swapping a={a} and b={b}")
