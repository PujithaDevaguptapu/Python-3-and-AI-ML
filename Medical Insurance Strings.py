medical_data = \
"""Marina Allison   ,27   ,   31.1 , 
#7010.0   ;Markus Valdez   ,   30, 
22.4,   #4050.0 ;Connie Ballard ,43 
,   25.3 , #12060.0 ;Darnell Weber   
,   35   , 20.6   , #7500.0;
Sylvie Charles   ,22, 22.1 
,#3022.0   ;   Vinay Padilla,24,   
26.9 ,#4620.0 ;Meredith Santiago, 51   , 
29.3 ,#16330.0;   Andre Mccarty, 
19,22.7 , #2900.0 ; 
Lorena Hodson ,65, 33.1 , #19370.0; 
Isaac Vu ,34, 24.8,   #7045.0"""

# Add your code here
print(medical_data)

#Replacing the '#' with '$'
updated_medical_data = medical_data.replace('#', '$')
print(updated_medical_data)

#To calculate the number of medical records
num_records = 0
for data in updated_medical_data:
  if data == '$':
    num_records += 1

print("There are {} medical records in the data.".format(num_records))

#Splitting the medical records into a list
medical_data_split = updated_medical_data.split(";")
print(medical_data_split)

#Splitting it futhur
medical_records = []
for data_split in medical_data_split:
  medical_records.append(data_split.split(","))

print(medical_records)

#Stripping the whitespace from all the lists
medical_records_clean = []
for cleaning in medical_records:
  record_clean = []
  for item in cleaning:
    record_clean.append(item.strip())
  medical_records_clean.append(record_clean)
 
print(medical_records_clean)

#Analyzing data 
#print names of 10 indiviuals
for record in medical_records_clean:
  print(record[0].upper())


#Storing different attribute
names = []
ages = []
bmis = []
insurance_costs = []

for record in medical_records_clean:
  names.append(record[0])
  ages.append(record[1])
  bmis.append(record[2])
  insurance_costs.append(record[3])

print(names)
print(ages)
print(bmis)
print(insurance_costs)

#Calculate average bmi
total_bmi = 0
for bmi in bmis:
  total_bmi += float(bmi)
print(total_bmi)

average_bmi = total_bmi/len(bmis)
print("Average BMI: {}".format(average_bmi))
