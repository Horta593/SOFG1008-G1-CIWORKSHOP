from meal import Meal 
from exceptions import InvalidConfirmationError

class Order:
    def __init__(self):
        self.meals = []

    def add_meal(self, meal, quantity):
        self.meals.append((meal, quantity))

    def get_total_cost(self):
        total_cost = 0.0
        total_quantity = 0

        for meal, quantity in self.meals:
            base_cost = meal.price
            if meal.is_special():
                base_cost *= 1.05

            cost = base_cost * quantity
            total_cost += cost
            total_quantity += quantity

        if total_quantity > 5:
            total_cost *= 0.9
        if total_quantity > 10:
            total_cost *= 0.8

        if total_cost > 100:
            total_cost -= 25
        elif total_cost > 50:
            total_cost -= 10

        return float(total_cost)

    def confirm_order(self):
        while True:
            try: 
                confirmation = input("Confirm your order (y/n): ")
                if confirmation.lower() == "y":
                    return True
                elif confirmation.lower() == "n":
                    return False
                else:
                    raise InvalidConfirmationError()
                
            except InvalidConfirmationError as confirmation_error:
                print(confirmation_error)
                continue