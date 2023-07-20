import unittest
from unittest.mock import patch, MagicMock
from meal import MealFactory
from order import Order

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


if __name__ == "__main__":
    unittest.main()
