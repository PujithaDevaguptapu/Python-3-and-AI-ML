import numpy

#Simulating binomial distribution using numpy library
print(numpy.random.binomial(n=1, p=0.8, size=500))

#Increased the number of trials by 100
print(numpy.random.binomial(n=100, p=0.8, size=500))
