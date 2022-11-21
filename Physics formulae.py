# Uncomment this when you reach the "Use the Force" section
train_mass = 22680
train_acceleration = 10
train_distance = 100
bomb_mass = 1


# Write your code below: 
# Fahrenheit funciton definition
def f_to_c(f_temp):
  c_temp = (f_temp - 32) * 5/9
  return c_temp

# Testing the function by assigning a variable
f100_in_celsius = f_to_c(100)

# Celsius function definition
def c_to_f(c_temp):
  f_temp = c_temp * (9/5) + 32
  return f_temp

# Testing the function by assining a variable
c0_in_fahrenheit = c_to_f(0)

# Defining a function 
def get_force(mass, acceleration):
  return mass * acceleration

# Testing the function 
train_force = get_force(train_mass, train_acceleration)
print(train_force)

# Newtons law of force
print("The GE train supplies " + str(train_force) + " Newtons of force.")

# Defining a function
def get_energy(mass, c = 3*10**8):
  return mass * (c**2)

# Testing energy
bomb_energy = get_energy(bomb_mass, c = 3*10**8)

print("A 1kg bomb supplies " + str(bomb_energy) + "Joules.")

# Do the work function definition
def get_work(mass, acceleration, distance):
  force = get_force(mass, acceleration)
  work = force * distance
  return work

# Testing work 
train_work = get_work(train_mass, train_acceleration, train_distance)

print("The GE train does " + str(train_work) + " Joules of work over " + str(train_distance) + " meters")
