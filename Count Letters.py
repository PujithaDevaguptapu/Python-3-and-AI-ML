# Program to count the number of unique letters in a string.
letters = "ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz"
# Writing unique_english_letters function here:
def unique_english_letters(word):
  count = 0
  for letter in letters:
    if letter in word:
      count += 1
  return count
# Uncomment these function calls to test your function:
print(unique_english_letters("mississippi"))
# should print 4
print(unique_english_letters("Apple"))
# should print 4
