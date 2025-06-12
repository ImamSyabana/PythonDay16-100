student_dict = {
    "student": ["Angela", "James", "Lily"], 
    "score": [56, 76, 98]
}

#Looping through dictionaries:
for (key, value) in student_dict.items():
    #Access key and value
    pass

import pandas
student_data_frame = pandas.DataFrame(student_dict)

#Loop through rows of a data frame
for (index, row) in student_data_frame.iterrows():
    #Access index and row
    #Access row.student or row.score
    pass

# Keyword Method with iterrows()
# {new_key:new_value for (index, row) in df.iterrows()}

#TODO 1. Create a dictionary in this format:
#{"A": "Alfa", "B": "Bravo"}

nato_alphabet_df = pandas.read_csv("Day 26/NATO-alphabet-start/nato_phonetic_alphabet.csv")
#print(nato_alphabet_df)

# for (index, row) in nato_alphabet_df.iterrows():
#     #print(index)
#     print(row.code)
#     print(row.letter)
    
phonetics_list = {row.letter:row.code for (index,row) in nato_alphabet_df.iterrows()}
print(phonetics_list)

#TODO 2. Create a list of the phonetic code words from a word that the user inputs.
user_name_input = input("Enter your name: ")
user_name_input = user_name_input.upper()

user_char_list = [char for char in user_name_input]
print(user_char_list)

user_phonetic_list = [phonetics_list[phonetic] for phonetic in user_char_list]
print(user_phonetic_list)