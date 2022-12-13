first_name = "Reiko"
last_name = "Matsuki"

def password_generator(first_name, last_name):
  length1 = len(first_name)
  length2 = len(last_name)
  new_string = first_name[length1-3:] + last_name[length2-3:]
  return new_string

temp_password = password_generator(first_name, last_name)
print(temp_password)
