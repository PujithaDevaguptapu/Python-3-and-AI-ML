#Generating a username 
def username_generator(first_name, last_name):
  if len(first_name) < 3 or len(last_name) < 4:
    user_name = first_name + last_name
  else:
    user_name = first_name[:3] + last_name[:4]
  return user_name

username_generator("Abe", "Simpson")

#Generating a password
def password_generator(user_name):
  password = ""
  for indi in range(0, len(user_name)):
    password += user_name[indi-1]
  return password

password_generator("AbeSimp")
