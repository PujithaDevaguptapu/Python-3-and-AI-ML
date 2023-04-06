#To see if a letter is in the given word
#Write your lambda function here
contains_a = lambda word: "a" in word

print(contains_a("banana"))
print(contains_a("apple"))
print(contains_a("cherry"))


#To see if the length of the given word is less or more than the desired length
#Write your lambda function here
long_string = lambda word: len(word) > 12

print(long_string("short"))
print(long_string("photosynthesis"))
