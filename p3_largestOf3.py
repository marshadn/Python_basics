a=int(input("Enter num1:"))
b=int(input("Enter num2:"))
c=int(input("Enter num3:"))

if a>b and a>c:
    print(f"The largest is:{a}")
elif b>c:
    print(f"The largest is:{b}")
else:
    print(f"The largest is:{c}")