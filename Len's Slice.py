# Your code below:
toppings = ["pepperoni", "pineapple", "cheese", "sausage", "olives", "anchovies", "mushrooms"]

prices = [2, 6, 1, 3, 2, 7, 2]

#sorting $2 slices 
num_two_dollar_slices = prices.count(2)
print(num_two_dollar_slices)

#Length of a variable
num_pizzas = len(toppings)
print(num_pizzas)

#Display of number of pizzas
print("We sell " + str(num_pizzas) + " different kinds of pizza!")

#Creating two dimenstional list with toppings and prices variable
pizza_and_prices = [[4, "Peas"], [5, "pineapple"], [10, "cheese"], [8, "sprouts"], [3, "olives"], [2, "Tomato"], [1, "Coriander"]]
print(pizza_and_prices)

#Sorting variable
pizza_and_prices.sort()
print(pizza_and_prices)

cheapest_pizza = pizza_and_prices[0]
priciest_pizza = pizza_and_prices[-1]

pizza_and_prices.pop(4)
print(pizza_and_prices)

#Adding new sublist
pizza_and_prices.insert(1, [2.5, "peppers"])
print(pizza_and_prices)

#last three chepeaset pizzas
three_cheapest = pizza_and_prices[-3:]
print(three_cheapest)

