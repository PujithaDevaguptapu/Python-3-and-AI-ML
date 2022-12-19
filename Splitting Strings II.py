authors = "Audre Lorde,Gabriela Mistral,Jean Toomer,An Qi,Walt Whitman,Shel Silverstein,Carmen Boullosa,Kamala Suraiyya,Langston Hughes,Adrienne Rich,Nikki Giovanni"

#Seperating author names
author_names = authors.split(',')
print(author_names)

#Printing only last names
author_last_names = []
for last in author_names:
  author_last_names.append(last.split()[-1])

print(author_last_names)
