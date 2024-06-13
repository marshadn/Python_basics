name=input("Enter the name:")
date=input("Enter the date:")

template='''
Dear |<name>|
You are selected on
|<date>|
'''

print(template.replace('|<name>|',name).replace('|<date>|',date))