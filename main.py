# Day 16 – Coffee Machine (Object-Oriented Programming)
# This version refactors the procedural coffee machine
# into separate classes with clear responsibilities.
#
# Goal:
# - Practice OOP concepts like classes, objects, methods, and separation of concerns
# - Make the code more modular, readable, and scalable

from menu import Menu
from coffee_maker import CoffeeMaker
from money_machine import MoneyMachine


# Create objects (instances) of each major system in the coffee machine
drink_menu = Menu()            # Handles available drinks and menu lookup
drink_maker = CoffeeMaker()    # Manages resources and coffee preparation
money_maker = MoneyMachine()  # Handles payment and profit tracking

# Flag to keep the coffee machine running
machine_on = True

# Main program loop
while machine_on:

    # Show available drinks dynamically from the Menu class
    user_order = input(f"What would you like? ({drink_menu.get_items()}): ")

    # Admin command: show machine status
    if user_order == "report":
        drink_maker.report()
        money_maker.report()

    # Admin command: turn off the machine
    elif user_order == "off":
        machine_on = False

    # Handle drink order
    else:
        # Find the requested drink as a MenuItem object
        user_drink = drink_menu.find_drink(user_order)

        # Only proceed if:
        # 1. There are enough ingredients
        # 2. Payment is successful
        if (
            drink_maker.is_resource_sufficient(user_drink)
            and money_maker.make_payment(user_drink.cost)
        ):
            # Make and serve the coffee
            drink_maker.make_coffee(user_drink)
