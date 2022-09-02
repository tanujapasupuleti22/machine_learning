sentence = "I am a teacher and I love to inspire and teach people"

# getting all words used in the sentence by using split() with space string
print("All words: " + str(sentence.split(' '))[1:-1])
# getting the unique words used in the sentence by converting the above list to set using set()
uniqueWords = set(sentence.split(' '))
print("Unique words: " + str(uniqueWords)[1:-1])

# getting the length of unique words used in the sentence by using len()
print("length of unique words: " + str(len(uniqueWords)))
