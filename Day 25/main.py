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

# alternatif
print(data["temp"].mean())

# nilai maksimum
print(data["temp"].max())

#mendapatkan data di columns
print(data["condition"])
print(data.condition) # case sensitive

# get specific data in a row of dataframe 
print(data[data["day"] == "Monday"])

# mengambil row data yang temperaturnya paling maksimum
print(data[data["temp"] == data["temp"].max()])

# mendapatkan informasi kolom yang ada pada baris tertentu dalam dataset
monday = data[data["day"] == "Monday"]
print(monday.condition) # sunny

# challenge: merubah temperature hari Monday dari celcius ke fahrenheit
print((int(monday.temp[0]) * 9/5) + 32)


## CREATE A DATAFRAME FROM SCRATCH
data_dict = {
    "students" : ["Amy", "James", "Angela"],
    "scores": [76, 56, 65]
}

data = pd.DataFrame(data_dict)
data.to_csv("Day 25/new_data.csv")