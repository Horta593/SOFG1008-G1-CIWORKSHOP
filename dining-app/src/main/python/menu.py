
from meal import MealFactory, ItalianMeal, ChineseMeal, ChefSpecials, PastriesMeal
from exceptions import InvalidQuantityError, InvalidMealError, InvalidConfirmationError
from order import Order
from quantity_validator import QuantityValidator
class Menu:
    def __init__(self):
        self.meals = {
            1: MealFactory.create_meal("Chinese", "Wantang", 12.00),
            2: MealFactory.create_meal("Pastries", "Puff pastry", 6.00),
            3: MealFactory.create_meal("Italian", "Pizza", 12.00),
            4: MealFactory.create_meal("ChefSpecials", "Chef's salad", 25.00),
            5: MealFactory.create_meal("ChefSpecials", "Chef's plato", 25.00)
        }
        self.available_meals = set(self.meals.keys()) 

    def display_menu(self):
        print("MENU:")
        print("-------")
        for meal_id, meal in self.meals.items():
            print(f"{meal_id}. {meal.name} - ${meal.price}")

    def select_meals(self):
        selected_meals = []
        while True:
            self.display_menu()
            meal_id = input("Enter the meal ID to select (or 'q' to quit): ")
            if meal_id == 'q':
                break
            meal_id = int(meal_id)
            if meal_id not in self.available_meals:
                print("Invalid meal ID. Please try again.")
                continue

            quantity = input("Enter the quantity: ")
            try:
                if not QuantityValidator.is_valid_quantity(quantity):
                    raise InvalidQuantityError()
                quantity = int(quantity)
            except InvalidQuantityError:
                print("Invalid quantity. Please enter a valid positive integer between 1 and 100.")
                continue

            selected_meals.append((meal_id, quantity))
        return selected_meals