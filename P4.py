#a sentence of words
sentence = "the cat and the hat and the bat"
word_count = {}
max_word = ""
max_count = 0

for word in sentence.split():
    word_count[word] = word_count.get(word, 0) + 1
  
    if word_count[word] > max_count:
       max_count = word_count[word]
       max_word = word

print(word_count)
print(f"{max_word}:{max_count}")


