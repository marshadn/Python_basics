a=76
b=45
c=6
d=23

if a>b:
    maxNum1=a
else:
    maxNum1=b

if c>d:
    maxNum2=c
else:
    maxNum2=d
    
if maxNum1>maxNum2:
    maxNum=maxNum1
else:
    maxNum=maxNum2
    
print(f"The greatest among {a},{b},{c},{d} is {maxNum}")
