import requests
import csv

r = requests.get('https://api.census.gov/data/2020/acs/acs5?get=NAME,B08303_001E,B08303_013E&for=county:*&in=state:36')

#json method to store data
r_json = r.json()

with open('commute_data.csv', mode='w', newline='') as file:
  writer = csv.writer(file)
  writer.writerows(r_json)
