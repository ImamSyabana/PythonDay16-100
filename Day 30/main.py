# # FileNotFound Error
# #file = open("a_file.txt")
# try:
#     file = open("Day 30/a_file.txt") # try to read non existing file
#     a_dictionary = {"key": "value"}
#     print(a_dictionary["key"])
    
# # print except jika adaa eror yang di try block
# except FileNotFoundError:
#     file = open("Day 30/a_file.txt", "w")
#     file.write("Something")
    
# except KeyError as error_message:
#     print(f"That key {error_message} does not exist")

# # print else jika di try block tidak ada error sama sekali
# else:
#     content = file.read()
#     print(content)
    
# # print finally pada saat di try block error atau tidak eror
# finally:
#     file.close()
#     print("file was closed.")


# membuat raise untuk mengeluarkan pesan error walaupun code ngga nge bug

height = float(input("Height: "))
weight = int(input("Weight: "))

if height > 3:
    raise ValueError("Human height should not be over 3 meters.")

bmi = weight / height ** 2 
print(bmi)

