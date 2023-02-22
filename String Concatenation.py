first_name = "Reiko"
last_name = "Matsuki"

#Function for last three letters in each string combined
def password_generator(first_name, last_name):
  length1 = len(first_name)
  length2 = len(last_name)
  return first_name[length1 - 3:] + last_name[length2 - 3:]

#Alternatively this function code works too
#def password_generator(first_name, last_name):
  #return first_name[len(first_name) - 3:] + last_name[len(last_name) - 3:]

#Calling function
temp_password = password_generator("Reiko", "Matsuki")
print(temp_password)
