#Welcoming users to application
def trip_planner_welcome(name):
  print("Welcome to tripplanner v1.0 " + name )

#calling the function 
trip_planner_welcome("Kanni")

#Defining a function for trip time
def estimated_time_rounded(estimated_time):
  rounded_time = round(estimated_time)
  return rounded_time

#calling the time function
estimate = estimated_time_rounded(2.7)

#Generating messages for user's planned trip
def destination_setup(origin, destination, estimated_time, mode_of_transport = "Car"):
  print("Your trip starts off in " + origin)
  print("And you are traveling to " + destination)
  print("You will be traveling by " + mode_of_transport)
  print("It will take approximately " + str(estimated_time) + " hours")

#Calling final function with arguments
destination_setup("Visakhapatnam", "Fredericton", estimate, "Train")

