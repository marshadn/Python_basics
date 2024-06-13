

# text=input("Enter your word here:")

# for i in text:
#     if i=='a'or i=='e'or i=='i'or i=='o'or i=='u':
#         print(list[i],end=" ")
        
# text = input("Enter your word here: ")

# vowels = ['a', 'e', 'i', 'o', 'u']

# for char in text:
#     if char.lower() in vowels:
#         print(char, end=" ")

word = input("Enter your word here: ")

vowels = [char for char in word if char.lower() in 'aeiou']

print(vowels)
