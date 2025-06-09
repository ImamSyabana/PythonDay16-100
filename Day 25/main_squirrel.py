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