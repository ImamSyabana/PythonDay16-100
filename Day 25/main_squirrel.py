import pandas as pd

data = pd.read_csv("Day 25/2018_Central_Park_Squirrel_Census_-_Squirrel_Data.csv")
#print(data)

num_squirrel = data["Primary Fur Color"]
print(type(num_squirrel)) # tipe series 

print(num_squirrel.value_counts())

# convert ke dataframe
df = pd.DataFrame(num_squirrel.value_counts())
print(df)
# Convert ke csv 
df.to_csv("Day 25_squirrel/jumlahTupai.csv")


## Cara Alternatif
#Central Park Squirrel Data Analysis
import pandas

data = pandas.read_csv("2018_Central_Park_Squirrel_Census_-_Squirrel_Data.csv")
grey_squirrels_count = len(data[data["Primary Fur Color"] == "Gray"])
red_squirrels_count = len(data[data["Primary Fur Color"] == "Cinnamon"])
black_squirrels_count = len(data[data["Primary Fur Color"] == "Black"])
print(grey_squirrels_count)
print(red_squirrels_count)
print(black_squirrels_count)

data_dict = {
    "Fur Color": ["Gray", "Cinnamon", "Black"],
    "Count": [grey_squirrels_count, red_squirrels_count, black_squirrels_count]
}

df = pandas.DataFrame(data_dict)
df.to_csv("squirrel_count.csv") 