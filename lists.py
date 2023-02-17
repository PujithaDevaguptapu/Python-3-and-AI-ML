# Your code below: 
#First list 
first_names = ["Ainsley", "Ben", "Chani", "Depak"]

#another list with sizes of first list
preferred_size = ["Small", "Large", "Medium"]

#Forgot to add last value using .append() method
preferred_size.append("Medium")
print(preferred_size)

# Two-dimenstional list
customer_data = [["Ainsley",	"Small",	True], ["Ben",	"Large",	False], ["Chani",	"Medium",	True], ["Depak",	"Medium",	False]]
print(customer_data)

#Changing value in a sublist
customer_data[2][2] = False
print(customer_data)

#Removing the value in a sublist
customer_data[1].remove(False)

#Adding sublists
customer_data_final = customer_data + [["Amit", "Large", True], ["Karim", "X-Large", False]]
print(customer_data_final)
