import requests

#Using get() method to request API and assiagning it to a variable
r = requests.get('https://api.census.gov/data/2020/acs/acs5?get=NAME,B08303_001E,B08303_013E&for=county:*&in=state:36')

#Using .text attribute to return the string data
r_text = r.text
print(r_text)

#Using .json() method 
r_json = r.json()
print(r_json)
