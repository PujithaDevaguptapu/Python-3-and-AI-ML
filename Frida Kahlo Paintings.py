#First, create a list called paintings and add the following titles to it:
#'The Two Fridas', 'My Dress Hangs Here', 'Tree of Hope', 'Self Portrait With Monkeys'

Print the master_list to the terminal.paintings = ['The Two Fridas', 'My Dress Hangs Here', 'Tree of Hope', 'Self Portrait With Monkeys']

#Next, create a second list called dates and give it the following values:
#1939, 1933, 1946, 1940

dates = [1939, 1933, 1946, 1940]

#It doesn’t do much good to have the paintings without their dates, and vice versa. Zip together the two lists so that each painting is paired with its date and resave it to the paintings variable. Make sure to convert the zipped object into a list using the list() function. Print the results to the terminal to check your work.

#Zipping two lists together and reassaigning to the list
paintings = list(zip(paintings, dates))
print(paintings)

#There were some last minute additions to the show that we need to add to our list. Append the following paintings to our paintings list then re-print to check they were added correctly:
#'The Broken Column', 1944, 'The Wounded Deer', 1946, 'Me and My Doll', 1937

#Appending the list
paintings.append(('The Broken Column', 1944))
paintings.append(('The Wounded Deer', 1946))
paintings.append(('Me and My Doll', 1937))
print(paintings)

#Since each of these paintings is going to be in the audio tour, they each need a unique identification number. But before we assign them a number, we first need to check how many paintings there are in total.
#Find the length of the paintings list.

print(len(paintings))


#Use the range method to generate a list of identification numbers that starts at 1 and is equal in length to our list of items. Save the list to the variable audio_tour_number and check your work by printing the list.

#Creating a list using range
audio_tour_number = range(1, len(paintings)+1)
print(list(audio_tour_number))

#We’re finally ready to create our master list. Zip the audio_tour_number list to the paintings list and save it as master_list.

#Zipping the audio list to the paintings list
master_list = list(zip(audio_tour_number, paintings))

#Print the master_list to the terminal.

print(master_list)
