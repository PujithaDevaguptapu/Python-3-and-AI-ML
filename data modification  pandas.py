import codecademylib3
import pandas as pd

#Load the data from the csv file
orders = pd.read_csv("shoefly.csv")
print(orders)

#print the first 5 lines of data
print(orders.head())

#Select all the column names into a variable
emails = orders.email
print(emails)

#Selecting multiple rows 
frances_palmer = orders[(orders.first_name == "Frances") & (orders.last_name == "Palmer")]
print(frances_palmer)

#Selecting rows using logic
comfy_shoes = orders[orders.shoe_type.isin(['clogs', 'boots', 'ballet flats'])]
print(comfy_shoes)
