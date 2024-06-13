# Sample dictionary
# sample_dict = {'apple': 5, 'banana': 2, 'orange': 8, 'grape': 1}

# # Sort the dictionary in ascending order by keys
# ascending_sorted_dict = dict(sorted(sample_dict.items()))

# # Sort the dictionary in descending order by keys
# descending_sorted_dict = dict(sorted(sample_dict.items(), reverse=True))

# # Print the original and sorted dictionaries
# print("Original Dictionary:", sample_dict)
# print("Ascending Sorted Dictionary:", ascending_sorted_dict)
# print("Descending Sorted Dictionary:", descending_sorted_dict)


dict1={1:"apple",6:"banana", 4:"mango",
       3:"grape", 7:"Blueberry",2:"pineapple"
       }

sortDict=dict(sorted(dict1.items()))
sortDesDict=dict(sorted(dict1.items(),reverse=True))

print(f"The ascending order is {sortDict}")
print(f"The descending order is {sortDesDict}")