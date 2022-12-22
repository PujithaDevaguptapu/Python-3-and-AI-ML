highlighted_poems = "Afterimages:Audre Lorde:1997,  The Shadow:William Carlos Williams:1915, Ecstasy:Gabriela Mistral:1925,   Georgia Dusk:Jean Toomer:1923,   Parting Before Daybreak:An Qi:2014, The Untold Want:Walt Whitman:1871, Mr. Grumpledump's Song:Shel Silverstein:2004, Angel Sound Mexico City:Carmen Boullosa:2013, In Love:Kamala Suraiyya:1965, Dream Variations:Langston Hughes:1994, Dreamwood:Adrienne Rich:1987"
print(highlighted_poems)

#Splitting the strings
highlighted_poems_list = highlighted_poems.split(",")
print(highlighted_poems_list)

#Removing Whitespaces
highlighted_poems_stripped = []
for items in highlighted_poems_list:
  highlighted_poems_stripped.append(items.strip(" "))

print(highlighted_poems_stripped)

#Creating list of lists
highlighted_poems_details = []
for sublist in highlighted_poems_stripped:
  highlighted_poems_details.append(sublist.split(":"))

print(highlighted_poems_details)

#Creating empty lists
titles = []
poets = []
dates = []

#Iterating for dividing data into lists
for details in highlighted_poems_details:
  titles.append(details[0])
  poets.append(details[1])
  dates.append(details[2])

#for loop using .format() string method
for p in range(0, len(highlighted_poems_details)):
  print("The poem {} was published by {} in {}".format(titles[p], poets[p], dates[p]))
  

