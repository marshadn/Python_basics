l1=[4,5,1]
l2=[3,2,2]

if len(l1)==len(l2):
    print("Both list are of SAME length")
    
else:
    print("Both list are of DIFFERENT length")

sum1=0  
for i in l1:
    sum1+=i
    
print("sum is",sum1)
    

sum2=0  
for k in l2:
    sum2+=k
    
print("sum is",sum2)
    

if sum1==sum2:
    print("Both list are of  SAME sum")
    
else:
    print("Both list are of DIFFERENT sum")


common=[]    
for j in l1:
    if j in l2:
        common.append(j)
    
    
if common:    
      print(f"There are common elements {common}")
      
else:
        print("NO common")
   
    
    