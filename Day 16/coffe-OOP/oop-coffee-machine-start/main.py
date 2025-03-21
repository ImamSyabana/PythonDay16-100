from menu import Menu
from coffee_maker import CoffeeMaker
from money_machine import MoneyMachine

print("Welcome to the Coffee Machine!")
menu = Menu()
coffee_maker = CoffeeMaker()
money_machine = MoneyMachine()


machine_isOn = True

while machine_isOn == True:
    order = str(input("What would you like? (espresso/latte/cappucinno): "))

    if order == 'off':
        machine_isOn = False
        break

    if order == 'report':
        print(coffee_maker.report())
        print(money_machine.report())
        
        continue

    isSufficient = coffee_maker.is_resource_sufficient(menu.find_drink(order))
    
    if isSufficient == False:
        continue
    
    
    # print("Please insert coins. ")
    # quarters_qnt = int(input("How many quarters?: "))
    # dimes_qnt = int(input("How many dimes?: "))
    # nickels_qnt = int(input("How many nickles?: "))
    # pennies_qnt = int(input("How many pennies?: "))

    # quarters = quarters_qnt * 0.25
    # dimes = dimes_qnt * 0.10
    # nickels = nickels_qnt * 0.05
    # pennies = pennies_qnt * 0.01

    # userMoney = quarters + dimes + nickels + pennies
    orderCost = menu.find_drink(order).cost

    isPaid = money_machine.make_payment(orderCost)

    if isPaid == False:
        continue
    elif isPaid == True:
        makeCoffee = coffee_maker.make_coffee(menu.find_drink(order))
        continue
    
 