# DICT Comprehension looping dari List

names = ["Alex", "Beth", "Carroline", "Dave", "Eleonora", "Freddie"]

import random
students_score = {student : random.randint(0,100) for student in names}

print(students_score)

# Dict comprehension looping dari dictionary lain
passed_student = {passed_name : score_name for (passed_name, score_name) in students_score.items() if score_name >= 60}
print(passed_student)