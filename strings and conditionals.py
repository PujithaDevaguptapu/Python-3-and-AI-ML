def letter_check(word, letter):
  for char in word:
    if char == letter:
      return True
  return False

print(letter_check("strawberry", "a"))
print(letter_check("strawberry", "o"))
print(letter_check("strawberry", "b"))



def contains(big_string, little_string):
  return little_string in big_string

def common_letters(string_one, string_two):
  common = []
  for letter in string_one:
    if (letter in string_two) and not (letter in common):
      common.append(letter)
  return common
