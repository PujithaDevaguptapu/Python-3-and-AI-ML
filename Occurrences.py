#Counting the occurrences in a given string
def count_char_x(word, x):
  count = 0 #To keep track of occurances in the string
  for letter in word:
    if x == letter:
      count += 1
  return count
# Uncomment these function calls to test your tip function:
print(count_char_x("mississippi", "s"))
# should print 4
print(count_char_x("mississippi", "m"))
# should print 1
