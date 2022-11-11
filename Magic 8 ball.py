import random
name = "Kanni"
question = "Did you let the dogs out?"
answer = ""
random_number = random.randint(1, 15)
# Used randint() function to randomly generate a number from the range 
if random_number == 1:
  answer = "Yes - definitely."
elif random_number == 2:
  answer = "It is decidedly so."
elif random_number == 3:
  answer = "Without a doubt."
elif random_number == 4:
  answer = "You may rely on it."
elif random_number == 5:
  answer = "As I see it, yes."
elif random_number == 6:
  answer = "Reply hazy, try again."
elif random_number == 7:
  answer = "Ask again later."
elif random_number == 8:
  answer = "Better not tell you now."
elif random_number == 9:
  answer = "Cannot predict now."
elif random_number == 10:
  answer = "Concentrate and ask again."
elif random_number == 11:
  answer = "My sources say no."
elif random_number == 12:
  answer = "Outlook not so good."
elif random_number == 13:
  answer = "Very doubtful."
elif random_number == 14:
  answer = "Dont count on it."
elif random_number == 15:
  answer = "My reply is no."
else:
  answer = "Error"

if name == "": 
  print("Question: " + question)
elif question == "":
  print("Please provide your question.")
else:
  print(name + " asks: " + question)
print("Magic 8-Ball's answer: " + answer)


  
