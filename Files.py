#Reading a file
with open("welcome.txt") as text_file:
  text_data = text_file.read()
  print(text_data)
  
#Iterating through lines
with open("how_many_lines.txt") as lines_doc:
  for read_lines in lines_doc.readlines():
    print(read_lines)
    
 
#Reading a single line
with open("just_the_first.txt") as first_line_doc:
  first_line = first_line_doc.readline()
  print(first_line)
