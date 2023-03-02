import csv
with open('cool_csv.csv', newline='') as cool_csv_file:
  cool_csv_dict = csv.DictReader(cool_csv_file)
  for row in cool_csv_dict:
    print(row)
