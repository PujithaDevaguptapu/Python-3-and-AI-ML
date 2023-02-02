def substring_between_letters(word, start, end):
  starting = word.find(start)
  ending = word.find(end)
  if starting > -1 and ending > -1:
    return (word[starting + 1 : ending])
  return word
# Uncomment these function calls to test your function:
print(substring_between_letters("apple", "p", "e"))
# should print "pl"
print(substring_between_letters("apple", "p", "c"))
# should print "apple"
