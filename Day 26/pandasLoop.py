student_dict = {
    "student" : ["Angela", "James", "Lily"],
    "score" : [56, 76, 98]
    
}

# Looping through dictionary
for (key,value) in student_dict.items():
    print(value)
    
# Looping through pandas
import pandas as pd 

student_data_frame = pd.DataFrame(student_dict)
print(student_data_frame)
print(type(student_data_frame))

# for (key, value) in student_data_frame.items():
#     print(value)
    
# looping pandas with iter rows
# loop through rows of a data frame
# index = column index, row = row data
for (index, row) in student_data_frame.iterrows():
    print(row.score)