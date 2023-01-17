zodiac_elements = {"water": ["Cancer", "Scorpio", "Pisces"], "fire": ["Aries", "Leo", "Sagittarius"], "earth": ["Taurus", "Virgo", "Capricorn"], "air":["Gemini", "Libra", "Aquarius"]}

zodiac_elements["energy"] = "Not a Zodiac element"

key_check = "energy"
#Checking if the key exists in dictonary
if key_check in zodiac_elements:
  print(zodiac_elements["energy"])

