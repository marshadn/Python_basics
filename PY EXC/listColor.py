li=[]

while True:
    inputList=input(("Enter the elements to the list:"))
    
    if inputList.lower()=='done':
        break
    else:
        li.append(inputList)
        
print(li)
li[0]=li[-1]
li[-1]=li[0]

print("The new list After Exchange",li)