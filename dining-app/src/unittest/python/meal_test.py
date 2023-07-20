import unittest
import sys
sys.path.append('src/main/python')
from meal import Meal, ChineseMeal, ItalianMeal, PastriesMeal, ChefSpecials, MealFactory

class TestMeal(unittest.TestCase):
    def test_meal_init(self):
        meal = Meal("Test Meal", 10.00, "Test")
        self.assertEqual(meal.name, "Test Meal")
        self.assertEqual(meal.price, 10.00)
        self.assertEqual(meal.category, "Test")

    def test_meal_str(self):
        meal = Meal("Test Meal", 10.00, "Test")
        self.assertEqual(str(meal), "Test Meal - $10.00")

    def test_meal_is_special(self):
        special_meal = ChefSpecials("Special Meal", 25.00)
        normal_meal = ItalianMeal("Normal Meal", 12.00)
        self.assertTrue(special_meal.category == "ChefSpecials")
    
    def test_meal_is_not_special(self):
        normal_meal = ItalianMeal("Normal Meal", 12.00)
        self.assertFalse(normal_meal.category == "ItalianMeal")

class TestChineseMeal(unittest.TestCase):
    def test_chinese_meal_init(self):
        chinese_meal = ChineseMeal("Wantang", 12.00)
        self.assertEqual(chinese_meal.name, "Wantang")
        self.assertEqual(chinese_meal.price, 12.00)
        self.assertEqual(chinese_meal.category, "Chinese")

class TestItalianMeal(unittest.TestCase):
    def test_italian_meal_init(self):
        italian_meal = ItalianMeal("Pizza", 14.00)
        self.assertEqual(italian_meal.name, "Pizza")
        self.assertEqual(italian_meal.price, 14.00)
        self.assertEqual(italian_meal.category, "Italian")

class TestPastriesMeal(unittest.TestCase):
    def test_pastries_meal_init(self):
        pastries_meal = PastriesMeal("Croissant", 6.50)
        self.assertEqual(pastries_meal.name, "Croissant")
        self.assertEqual(pastries_meal.price, 6.50)
        self.assertEqual(pastries_meal.category, "Pastries")

class TestChefSpecials(unittest.TestCase):
    def test_chef_specials_init(self):
        chef_specials = ChefSpecials("Special Salad", 18.00)
        self.assertEqual(chef_specials.name, "Special Salad")
        self.assertEqual(chef_specials.price, 18.00)
        self.assertEqual(chef_specials.category, "ChefSpecials")

class TestMealFactory(unittest.TestCase):
    def test_create_chinese_meal(self):
        meal = MealFactory.create_meal("Chinese", "Dim Sum", 10.00)
        self.assertIsInstance(meal, ChineseMeal)

    def test_create_italian_meal(self):
        meal = MealFactory.create_meal("Italian", "Pasta", 12.00)
        self.assertIsInstance(meal, ItalianMeal)

    def test_create_pastries_meal(self):
        meal = MealFactory.create_meal("Pastries", "Croissant", 6.50)
        self.assertIsInstance(meal, PastriesMeal)

    def test_create_chef_specials(self):
        meal = MealFactory.create_meal("ChefSpecials", "Special Salad", 18.00)
        self.assertIsInstance(meal, ChefSpecials)

    def test_create_invalid_meal_type(self):
        with self.assertRaises(ValueError):
            MealFactory.create_meal("InvalidType", "Invalid Meal", 10.00)

if __name__ == '__main__':
    unittest.main()