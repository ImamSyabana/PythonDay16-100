# Challenge 15
numbers = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55]
squared_numbers = [num ** 2 for num in numbers]
print(squared_numbers)

# challenge 16
list_of_strings = ['9', '0', '32', '8', '2', '8', '64', '29', '42', '99']
numbers = [int(conv) for conv in list_of_strings]
result = [intgr for intgr in numbers if intgr % 2 == 0]
print(result)

# Challenge 17
file1 = open("file1.txt")
file1_num = [n1 for n1 in file1.readlines()]

file2 = open("file2.txt")
file2_num = [n2 for n2 in file2.readlines()]

result = [int(n1n2.strip("\n")) for n1n2 in file1_num if n1n2 in file2_num]

print(result)

file1.close()
file2.close()