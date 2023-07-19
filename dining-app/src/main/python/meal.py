class Meal:
    def __init__(self, name, price):
        self.name = name
        self.price = price

    def __str__(self):
        return f"{self.name} - ${self.price:.2f}"


class ChineseMeal(Meal):
    def __init__(self, name, price):
        super().__init__(name, price)


class ItalianMeal(Meal):
    def __init__(self, name, price):
        super().__init__(name, price)


class PastriesMeal(Meal):
    def __init__(self, name, price):
        super().__init__(name, price)


class ChefSpecials(Meal):
    def __init__(self, name, price):
        super().__init__(name, price)


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