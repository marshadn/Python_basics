
def isPrime(num):
    
    if num==1:
        return f"1 is neither prime nor composite"
    for i in range(2,num):       
            
        if num%i==0:
            return f"{num} is NOT a prime number"
            
        
        
    return f"{num} is a prime number"
            
        
num=int(input("Enter the number:"))
print(isPrime(num))
            