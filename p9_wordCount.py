# Input: Sentence
# sentence = "This is a sample sentence without using functions."
sentence=input("Enter the sentance:")
word_count = 0

# Iterate through each character in the sentence
for char in sentence:
    # Check if the character is a space (indicating the end of a word)
    if char == ' ':
        word_count += 1

# Increment word_count by 1 to account for the last word
word_count += 1

print(f"The number of words in the sentence is: {word_count}")
