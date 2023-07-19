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


class Extra(Meal):
    pass


class MealFactory:
    @staticmethod
    def create_meal(meal_type, name, cost):
        if meal_type == "starter":
            return Starter(name, cost)
        elif meal_type == "main":
            return Main(name, cost)
        elif meal_type == "extra":
            return Extra(name, cost)
        else:
            raise ValueError("Invalid meal type.")

    @staticmethod
    def get_predefined_meals(meal_type):
        starter_meals = [
            Starter("Papitas", 7.5),
            Starter("Pan de ajo", 4.0),
        ]
        main_meals = [
            Main("Comida media cara", 15.0),
            Main("Comida cara", 11.0),
        ]
        extra_meals = [
            Extra("Brownie lokote", 5.0),
            Extra("Yuquitas", 3.5),
        ]

        if meal_type == "starter":
            return starter_meals
        elif meal_type == "main":
            return main_meals
        elif meal_type == "extra":
            return extra_meals
        else:
            raise ValueError("Invalid meal type.")