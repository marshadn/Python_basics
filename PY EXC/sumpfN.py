def sum(n):
    if n==0:
        return 0
    else:
        return n+sum(n-1)
        
        
    


n=int(input("Enter how many terms:"))
x=sum(n)
print(x)