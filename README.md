# Project-16---Coffee-Machine-Object-Oriented-Programming-

This is a beginner-to-intermediate Python project built as part of my 100 Days of Code challenge.

The goal of this project is to simulate a coffee machine using Object-Oriented Programming, focusing on clean separation of responsibilities and real-world system modeling.

**Project Overview**

The Coffee Machine OOP allows a user to:

Choose a drink (espresso / latte / cappuccino)

Insert coins to pay for the drink

Receive change if applicable

View machine reports (resources & money)

Turn the machine off

The program coordinates multiple classes that each represent a real component of a coffee machine.

**Why this project exists**

This project represents a key transition from procedural programming to OOP.
Instead of one large script, the logic is split into focused classes that are easier to read, extend, and maintain.

It helped reinforce how complex systems are easier to manage when responsibilities are clearly separated.

**What I learned**

How to design and use multiple interacting classes

How to model real-world objects using OOP

How to separate concerns across files and modules

How constructors (__init__) manage state

How objects communicate through method calls

How OOP improves scalability and readability

**How the code works (step-by-step)**

The Menu class stores available drinks and provides lookup functionality.

Each drink is represented by a MenuItem object containing ingredients and cost.

The CoffeeMaker class tracks machine resources and prepares drinks.

The MoneyMachine class handles coin input, payments, change, and profit.

main.py controls the program loop and coordinates all components.

The machine continues running until the user turns it off.

**Project File Structure**

├── main.py              # Program entry point and main loop

├── menu.py              # Menu and MenuItem classes

├── coffee_maker.py      # Resource tracking and coffee preparation

├── money_machine.py     # Coin processing, payments, and profit tracking

**Example Output**

What would you like? (latte/espresso/cappuccino/):

latte

Please insert coins.

How many quarters?: 10

Here is $0.0 in change.

Here is your latte ☕️. Enjoy!
