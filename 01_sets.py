#Collection of non repetitive elements
'''properties of sets
   1.Unique values
   2.Elements are unordered(order doesn't matter)
   3.Unindexzed(You can't access elements by indexing)
   4.There is no way to change items in sets
   5.Sets cannot contain duplicate values
'''
s={1,3,5,8,6}
s.add(23)
s.add(1) # not going to add bcz already present
#but blow can be added
# s.add("1")
# print(s)
# s.remove(8)
# print(s)
# s.pop()
# print(s)
# print(len(s))
#s.clear() is used empties the set


print(s.union({8,11}))
print(s.intersection({8,11}))
