class Meal:
    def __init__(self, name, cost):
        self.name = name
        self.cost = cost

    def calculate_cost(self, quantity):
        return self.cost * quantity


class Starter(Meal):
    pass


class Main(Meal):
    pass


class Dessert(Meal):
    pass


class MealFactory:
    @staticmethod
    def create_meal(meal_type, name, cost):
        if meal_type == "starter":
            return Starter(name, cost)
        elif meal_type == "main":
            return Main(name, cost)
        elif meal_type == "dessert":
            return Dessert(name, cost)
        else:
            raise ValueError("Invalid meal type.")

    @staticmethod
    def get_predefined_meals(meal_type):
        # Define the predefined meals for each type
        starter_meals = [
            Starter("Caesar Salad", 7.5),
            Starter("Garlic Bread", 4.0),
        ]
        main_meals = [
            Main("Grilled Salmon", 15.0),
            Main("Vegetable Curry", 11.0),
        ]
        dessert_meals = [
            Dessert("Chocolate Brownie", 5.0),
            Dessert("Fruit Salad", 3.5),
        ]

        if meal_type == "starter":
            return starter_meals
        elif meal_type == "main":
            return main_meals
        elif meal_type == "dessert":
            return dessert_meals
        else:
            raise ValueError("Invalid meal type.")