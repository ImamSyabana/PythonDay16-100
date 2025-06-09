## MEMBACA DATA CSV TANPA LIBRARY
data = []

weather_data = open("Day 25/weather_data.csv", "r")
for x in weather_data.readlines():
    data.append(x)
weather_data.close()

print(data)

## MEMBACA DATA CSV DENGAN LIBRARY CSV
import csv
with open("Day 25/weather_data.csv", "r") as data_file:
    data = csv.reader(data_file)
    temperatures = []
    for row in data:
        if row[1] == "temp":
            continue
        temperatures.append(int(row[1]))
    
    print(temperatures)      
        
## MEMBACA DATA CSV DENGAN LIBRARY PANDAS

import pandas as pd

data = pd.read_csv("Day 25/weather_data.csv")

#print(type(data))
#print(data["temp"])

data_dict = data.to_dict()
print(data_dict)

print(data["temp"].tolist())

# Pause 1: Average of the temperature value
temp_list = data["temp"].tolist()
sum_temp = sum(temp_list[:])
average_temp = sum_temp / len(temp_list)
print(average_temp)