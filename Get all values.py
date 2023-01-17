num_exercises = {"functions": 10, "syntax": 13, "control flow": 15, "loops": 22, "lists": 19, "classes": 18, "dictionaries": 18}

total_exercises = 0
for added_values in num_exercises.values():
  total_exercises += added_values

print(total_exercises)  
