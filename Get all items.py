pct_women_in_occupation = {"CEO": 28, "Engineering Manager": 9, "Pharmacist": 58, "Physician": 40, "Lawyer": 37, "Aerospace Engineer": 9}

#for loop to iterate through items
for company, value in pct_women_in_occupation.items():
  print("Women make up " + str(value) + " percent of " + company+"s.")
