# Challenge 18
sentence = "What is the Airspeed Velocity of an Unladen Swallow?"
result = {words: len(words) for words in sentence.split()}

# Challenge 19
weather_c = {"Monday": 12, "Tuesday": 14, "Wednesday": 15, "Thursday": 14, "Friday": 21, "Saturday": 22, "Sunday": 24}

weather_f = {days: round(((cel_to_fah * (9/5)) + 32), 1) for (days, cel_to_fah) in weather_c.items()}

print(weather_f)
