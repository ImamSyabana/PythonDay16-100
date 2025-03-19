from prettytable import PrettyTable

table = PrettyTable()
print(table)

table.add_column("Pokemon Name", ["Pikachu", "Squirtle", "Charmander", "Sprigatitto"]) 
table.add_column("Type", ["Electric", "Water", "Fire", "Grass"])
print(table)

print(table.align)

table.align = "l" # left align

print(table)
print(table.align)