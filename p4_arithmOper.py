a=int(input("Enter num1:"))
b=int(input("Enter num2:"))

op=input("Enter the operator:")

if(op=='+'):
    print(f"{a} + {b} = {a+b}")
    
elif(op=='-'):
    print(f"{a} - {b} = {a-b}")
    
elif(op=='*'):
    print(f"{a} * {b} = {a*b}")
    
elif(op=='/'):
    print(f"{a} / {b} = {a/b}")
    
else:
    print("Invalid operator")

