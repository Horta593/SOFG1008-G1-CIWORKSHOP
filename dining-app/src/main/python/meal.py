class Meal:
    def __init__(self, name, price, category):
        self.name = name
        self.price = price or 5.00
        self.category = category

    def __str__(self):
        return f"{self.name} - ${self.price:.2f}"

    def is_special(self):
        return self.category == "ChefSpecials"

class ChineseMeal(Meal):
    def __init__(self, name, price):
        super().__init__(name, price, "Chinese")

class ItalianMeal(Meal):
    def __init__(self, name, price):
        super().__init__(name, price, "Italian")

class PastriesMeal(Meal):
    def __init__(self, name, price):
        super().__init__(name, price, "Pastries")



class ChefSpecials(Meal):
    def __init__(self, name, price):
        super().__init__(name, price, "ChefSpecials")

class MealFactory:
    @staticmethod
    def create_meal(meal_type, name, price):
        if meal_type == "Chinese":
            return ChineseMeal(name, price)
        elif meal_type == "Italian":
            return ItalianMeal(name, price)
        elif meal_type == "Pastries":
            return PastriesMeal(name, price)
        elif meal_type == "ChefSpecials":
            return ChefSpecials(name, price)
        else:
            raise ValueError("Invalid meal type!")