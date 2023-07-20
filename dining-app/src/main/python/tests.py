import unittest
from unittest.mock import patch, MagicMock
from meal import MealFactory
from order import Order
import xmlrunner

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

class TestOrder(unittest.TestCase):
    def setUp(self):
        self.order = Order()

    def test_add_meal(self):
        meal_1 = MealFactory.create_meal("Italian","Pizza", 10.00)
        meal_2 = MealFactory.create_meal("ChefSpecials","Chef's salad", 25.00)
        self.order.add_meal(meal_1, 1)
        self.order.add_meal(meal_2, 2)
        self.assertEqual(len(self.order.meals), 2)
        self.assertEqual(self.order.meals[0], (meal_1, 1))
        self.assertEqual(self.order.meals[1], (meal_2, 2))

    def test_get_total_cost_quantity_discount_5(self):
        meal1 = MealFactory.create_meal("Chinese","Wantang", 12.00)
        self.order.add_meal(meal1, 6)
        total_cost = self.order.get_total_cost()
        self.assertEqual(total_cost, 54.8)

    
    def test_get_total_cost_quantity_discount_10(self):
        meal1 = MealFactory.create_meal("Chinese","Wantang", 12.00)
        self.order.add_meal(meal1, 11)
        total_cost = self.order.get_total_cost()
        self.assertEqual(total_cost, 85.04)
    
    def test_get_total_cost_special_offer_discount_50(self):
        meal1 = MealFactory.create_meal("Italian","Pizza", 12.00)
        self.order.add_meal(meal1, 5)
        total_cost = self.order.get_total_cost()
        #- 10
        self.assertEqual(total_cost, 50.0)
    
    def test_get_total_cost_special_offer_discount_100(self):
        meal1 = MealFactory.create_meal("Italian","Pizza", 12.00)
        self.order.add_meal(meal1, 11)
        total_cost = self.order.get_total_cost()
        #- 25
        self.assertEqual(total_cost, 85.04)

    def test_get_total_cost(self):
        meal1 = MealFactory.create_meal("Chinese","Wantang", 12.0)
        meal2 = MealFactory.create_meal("Italian","Pizza", 12.00,)
        self.order.add_meal(meal1, 2)
        self.order.add_meal(meal2, 1)
        self.assertEqual(self.order.get_total_cost(), 36.0)

    @patch('builtins.input', return_value='y')
    def test_confirm_order(self, mock_input):
        self.assertTrue(self.order.confirm_order())

    @patch('builtins.input', return_value='n')
    def test_confirm_order_negative(self, mock_input):
        self.assertFalse(self.order.confirm_order())


if __name__ == '__main__':
    unittest.main(testRunner=xmlrunner.XMLTestRunner(output='test-reports'))