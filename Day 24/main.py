# reading a file with a close statement
file = open('Day 24/my_file.txt')
contents = file.read()
print(contents)
file.close()

# Reading a file
with open("Day 24/my_file.txt") as file:
    content = file.read()
    print(content)
    
# Writing a file
with open("Day 24/my_file.txt", mode = "a") as file:
    file.write("\nnew text")
    
# Writing a new file that doest exist 
with open("Day 24/new_file.txt", mode = "w") as file:
    file.write("sadasdawdasda")
    