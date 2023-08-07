from menu import Menu, MenuItem
from coffee_maker import CoffeeMaker
from money_machine import MoneyMachine

money_machine = MoneyMachine()
coffee_maker = CoffeeMaker()
menu = Menu()

is_on = True

while is_on:
    # Gets the options from the menu
    options = menu.get_items()
    # Asks the customer what option the would like
    choice = input(f"What would you like? ({options}): ")
    # If customer types off, shuts the coffee machine off
    if choice == "off":
        is_on = False
    # If customer types report, gives list of resources and money in the machine 
    elif choice == "report":
        coffee_maker.report()
        money_machine.report()
    # Checks to see if the item typed is in the menu
    else:
        drink = menu.find_drink(choice)
        # Checks to see if the coffee machine has enough resources and money, then gives the customer their drink
        if coffee_maker.is_resource_sufficient(drink) and money_machine.make_payment(drink.cost):
            coffee_maker.make_coffee(drink)
