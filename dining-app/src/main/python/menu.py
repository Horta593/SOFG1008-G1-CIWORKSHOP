
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

#TODO: Implement menu