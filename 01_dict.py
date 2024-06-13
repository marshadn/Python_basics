dict={
    "Youtube":"A video sharing platform",
    "c++":"Most powerful Language",
    "Java":"Usually complex Syntax",
    "List":[0,4,8,2]
}

#print(dict)
#print(dict['List'])
#print(dict['Java'])
'''Properties
 1.Unordered
 2.Mutable
 3.(Indexed)
 4.Duplication is not allowed
'''
#print(dict.items())
#for a,b in dict.items():
#    print(a,":",b)

#for key in dict.keys():
#    print(key)

'''dict.update({"Marshad":"A good boy","mylist":[77,67,34]})
print(dict)'''

print(dict['c++'])
print(dict.get("Python")) #Python key is not present in the dict so it shows none