# List Comprehension

numbers = [1, 2, 3]
new_numbers = [num + 1 for num in numbers]
print(new_numbers)

name = "Angela"
name_char = [char for char in name]
print(name_char)

range_list = [num * 2 for num in range(1,5)]
print(range_list)

names = ["Alex", "Beth", "Carroline", "Dave", "Eleonora", "Freddie"]
short_names = [name_short for name_short in names if len(name_short) < 5]
print(short_names)

long_names = [long_nms.upper() for long_nms in names if len(long_nms) > 5]
print(long_names)