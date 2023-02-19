# Your code below:
single_digits = list(range(0, 10))

#Square list
squares = []
for digits in single_digits:
  print(digits)
  squares.append(digits ** 2)
print(squares)

#cubes 
cubes = [cube ** 3 for cube in single_digits]
print(cubes)

