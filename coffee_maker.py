class CoffeeMaker:
    """
    Models the physical coffee machine.
    Responsible for:
    - Tracking ingredient resources
    - Checking availability
    - Making coffee
    """

    def __init__(self):
        # Initial machine resource levels
        self.resources = {
            "water": 300,   # ml
            "milk": 200,    # ml
            "coffee": 100,  # grams
        }

    def report(self):
        """Prints the current resource levels in the machine."""
        print(f"Water: {self.resources['water']}ml")
        print(f"Milk: {self.resources['milk']}ml")
        print(f"Coffee: {self.resources['coffee']}g")

    def is_resource_sufficient(self, drink):
        """
        Checks if enough ingredients exist for the selected drink.

        Args:
            drink (MenuItem): The drink the user wants

        Returns:
            True if resources are sufficient, otherwise False
        """
        can_make = True

        for item in drink.ingredients:
            if drink.ingredients[item] > self.resources[item]:
                print(f"Sorry there is not enough {item}.")
                can_make = False

        return can_make

    def make_coffee(self, order):
        """
        Deducts ingredients from resources and serves the coffee.

        Args:
            order (MenuItem): The drink being prepared
        """
        for item in order.ingredients:
            self.resources[item] -= order.ingredients[item]

        print(f"Here is your {order.name} ☕️. Enjoy!")
