weight = 82
# Ground Shipping
if weight <= 2:
  print("Cost of  Ground Shipping the package:$" , weight * 1.50 + 20.00)
elif weight > 2 and weight <= 6:
  print("Cost of Ground Shipping the package:$" , weight * 3.00 + 20.00)
elif weight > 6 and weight <= 10:
  print("Cost of Ground Shipping the package:$" , weight * 4.00 + 20.00)
else:
  print("Cost of Ground Shipping the package:$" , weight * 4.75 + 20.00)

  # Ground Shipping Premium
premium_ground_shipping = 125.00
print("Cost of Premium Ground Shipping the package: $" , premium_ground_shipping )

# Drone Shipping 
if weight <= 2:
  drone_shipping = weight * 4.50 + 0.00
  print("Cost of Drone Shipping the package:$" , drone_shipping)
elif weight > 2 and weight <= 6:
  drone_shipping = weight * 9.00 + 0.00
  print("Cost of Drone Shipping the package:$" , drone_shipping)
elif weight > 6 and weight <= 10:
  drone_shipping = weight * 12.00 + 0.00
  print("Cost of Drone Shipping the package:$" , drone_shipping)
else:
  drone_shipping = weight * 14.25 + 0.00
  print("Cost of Drone Shipping the package:$" , drone_shipping)
