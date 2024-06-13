lis=input("Enter the numbers for the list:")

newList=lis.split()




myList=['over' if num >100 else num for num in newList ]

print(myList)
