# Sample dictionaries
dict1 = {'a': 1, 'b': 2}
dict2 = {'c': 3, 'd': 4}

# Merge dictionaries using the update method
# merged_dict = dict1.copy()  # Create a copy of the first dictionary
# merged_dict.update(dict2)   # Update it with the second dictionary

# # Print the merged dictionary
# print("Merged Dictionary:", merged_dict)
# x=dict1.copy()
# x.update(dict2)

# print(x)

mergedDict={**dict1,**dict2}
print(mergedDict)