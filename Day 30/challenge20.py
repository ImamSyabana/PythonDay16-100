fruits = ["Apple", "Pear", "Orange"]

# Catch the exception and make sure the code runs without crashing.
try:
    def make_pie(index):
        fruit = fruits[index]
        print(fruit + " pie")
    

    make_pie(4)
    
except IndexError:
    print("Fruit pie")


