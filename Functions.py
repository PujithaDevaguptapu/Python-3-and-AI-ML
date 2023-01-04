#with two or more parameters
def print_pattern(num_rows, char):
	for i in range(num_rows):
		for num_cols in range(num_rows-i):
			print(char, end="")
		print()
    
    
# Return a value
def get_first_even(seq):
    for elem in seq:
        if elem % 2 == 0:
            return elem
    else:
        return None
      
 # Recursion 
def fibonacci(n):
    if n == 0 or n == 1:
        return n
    else:
        return fibonacci(n-1) + fibonacci(n-2)
