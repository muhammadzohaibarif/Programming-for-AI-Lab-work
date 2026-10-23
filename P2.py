word = "Programming"

#word ko completely reverse karne ke liye hum ::-1 use karte hain
print(word[::-1])

#wohi process ho humne problem 1 ma kiya tha plus slicing bi
print(f"{word[0:3] } , {   word[8:11]}")
#count k lia hum diye ge variable ka name k saath .count() method use karte hain
print(word.count("m"))


#testing the words like python and level
words = ["level","python"]
for word in words:
    if  word == word[::-1]:
        print(True)
    else:
        print(False)