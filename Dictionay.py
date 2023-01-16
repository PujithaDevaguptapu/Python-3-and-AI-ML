songs = ["Like a Rolling Stone", "Satisfaction", "Imagine", "What's Going On", "Respect", "Good Vibrations"]
playcounts = [78, 29, 44, 21, 89, 5]

#Dictionary comprehension
plays = {songs:playcounts for songs, playcounts in zip(songs, playcounts)}
print(plays)

#Adding new entry
plays["Purple Haze"] = 1
#overwriting the value to key
plays["Respect"] = 94

#Creating a new dictionary with multiple keys using .update() method
library = {}
library.update({"The Best Songs": plays, "Sunday Feelings": {}})
print(library)
