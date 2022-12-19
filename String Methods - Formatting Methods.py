poem_title = "spring storm"
poem_author = "William Carlos Williams"

#Using lower() string method
poem_title_fixed  = poem_title.title()
print(poem_title)
print(poem_title_fixed)

#Using upper() string method
poem_author_fixed = poem_author.upper()
print(poem_author)
print(poem_author_fixed)

#Splitting Strings
line_one = "The sky has given over"

line_one_words = (line_one.split(""))
print(line_one_words)
