#list of squares of even numbers from 0 to 10
List =[]
for i in range(1,11):
    if i % 2 ==0:
        List.append(i*i)
print(List)


#mapping each word to its length

words = ["ai", "python", "data"]
list1 =[]
for word in words:
    list1.append(f"{word}:{len(word)}")
print(list1)

#sorting the word banana
word = "banana"
result = sorted(set(word))
print(result)




