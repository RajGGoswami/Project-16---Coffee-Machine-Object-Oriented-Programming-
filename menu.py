class MenuItem:
    """
    Models a single drink item on the menu.
    Stores:
    - Name
    - Cost
    - Required ingredients
    """

    def __init__(self, name, water, milk, coffee, cost):
        self.name = name
        self.cost = cost
        self.ingredients = {
            "water": water,
            "milk": milk,
            "coffee": coffee
        }


class Menu:
    """
    Models the drink menu.
    Responsible for:
    - Storing all available drinks
    - Displaying menu options
    - Confirming drink availability
    """

    def __init__(self):
        # List of MenuItem objects
        self.menu = [
            MenuItem(name="latte", water=200, milk=150, coffee=24, cost=2.5),
            MenuItem(name="espresso", water=50, milk=0, coffee=18, cost=1.5),
            MenuItem(name="cappuccino", water=250, milk=50, coffee=24, cost=3),
        ]

    def get_items(self):
        """
        Returns a formatted string of available drink names
        for display in the user prompt.
        """
        options = ""
        for item in self.menu:
            options += f"{item.name}/"
        return options

    def find_drink(self, order_name):
        """
        Searches for a drink by name.

        Args:
            order_name (str): User input drink name

        Returns:
            MenuItem if found, otherwise None
        """
        for item in self.menu:
            if item.name == order_name:
                return item

        print("Sorry that item is not available.")
