myList=[]

while True:
    inputList=input("Enter the elements to the list:")
    
    if inputList.lower() =='done' :
        break
    
    myList.append(inputList)
    
print("The list is",myList)