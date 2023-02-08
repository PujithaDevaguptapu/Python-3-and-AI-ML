#Change or add elements
import array as arr  
numbers = arr.array('i', [1, 2, 3, 5, 7, 10])  
   
# changing first element  
numbers[0] = 0     
print(numbers)    # Output: array('i', [0, 2, 3, 5, 7, 10])  
   
# changing 3rd to 5th element  
numbers[2:5] = arr.array('i', [4, 6, 8])    
print(numbers)    # Output: array('i', [0, 2, 4, 6, 8, 10])  

#Delete elements
import array as arr  
number = arr.array('i', [1, 2, 3, 3, 4])  
del number[2]                           # removing third element  
print(number)                           # Output: array('i', [1, 2, 3, 4])  

#Finding length of an element
