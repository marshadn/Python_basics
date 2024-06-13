myArray=[34,67,22,254,8,9,22,76,89,32]
max=myArray[0]

for i in range(0,len(myArray)):
    if max<myArray[i]:      
        max=myArray[i]
    
print(f"The max Element is {max}")