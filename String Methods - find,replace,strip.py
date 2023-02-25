#.find() method
god_wills_it_line_one = "The very earth will disown you"

disown_placement = god_wills_it_line_one.find("disown")
print(disown_placement)
#Output: 20 <- shows the index value of that string we searched for


#.replace() method
toomer_bio = \
"""
Nathan Pinchback Tomer, who adopted the name Jean Tomer early in his literary career, was born in Washington, D.C. in 1894. Jean is the son of Nathan Tomer was a mixed-race freedman, born into slavery in 1839 in Chatham County, North Carolina. Jean Tomer is most well known for his first book Cane, which vividly portrays the life of African-Americans in southern farmlands.
"""

toomer_bio_fixed = toomer_bio.replace("Tomer", "Toomer")
print(toomer_bio_fixed)

#.strip() method
love_maybe_lines = ['Always    ', '     in the middle of our bloodiest battles  ', 'you lay down your arms', '           like flowering mines    ','\n' ,'   to conquer me home.    ']

love_maybe_lines_stripped = []
for lines in love_maybe_lines:
  love_maybe_lines_stripped.append(lines.strip())

print(love_maybe_lines_stripped)

love_maybe_full = '\n'.join(love_maybe_lines_stripped)
print(love_maybe_full)
