li=['buy now','click this','subscribe this']

email=input("Enter the email:").lower()
spam=False

if 'buy now' in email:
    spam=True

if 'subscribe this' in email:
    spam=True
    
if 'click this' in email:
    spam=True
    
print(f"The spam is {spam}")