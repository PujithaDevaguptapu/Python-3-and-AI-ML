love_maybe_lines = ['Always    ', '     in the middle of our bloodiest battles  ', 'you lay down your arms', '           like flowering mines    ','\n' ,'   to conquer me home.    ']

#Removing whitespaces on every string
love_maybe_lines_stripped = []
for lines in love_maybe_lines:
  love_maybe_lines_stripped.append(lines.strip())

print(love_maybe_lines_stripped)

#Joining lines into one large string
love_maybe_full = "\n".join(love_maybe_lines_stripped)
print(love_maybe_full)

