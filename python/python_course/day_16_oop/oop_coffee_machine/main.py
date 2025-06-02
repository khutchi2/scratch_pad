from menu import Menu
from coffee_maker import CoffeeMaker
from money_machine import MoneyMachine

# Instatiate objects
coffee_maker: CoffeeMaker = CoffeeMaker()
money_machine: MoneyMachine = MoneyMachine()
menu: Menu = Menu()

# Print report
print("OOP Coffee Maker ready for action! \n")
print("Current report: \n")
coffee_maker.report()

is_on = True

is_on = True

while is_on:
    options = menu.get_items()
    choice = input(f"What would you like? ({options}): ")
    
    if choice == "off":
        is_on = False
    elif choice == "report":
        coffee_maker.report()
        money_machine.report()
    else:
        drink = menu.find_drink(choice)
        print(f"\n {drink.name} costs {drink.cost} \n")
        if coffee_maker.is_resource_sufficient(drink) and money_machine.make_payment(drink.cost):
          coffee_maker.make_coffee(drink)

