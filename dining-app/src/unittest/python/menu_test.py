import unittest
from unittest.mock import patch, MagicMock
from src.main.python.menu import Menu
from src.main.python.meal import Meal
from src.main.python.exceptions import InvalidQuantityError, InvalidMealError

class TestMenu(unittest.TestCase):
    def setUp(self):
        self.menu = Menu()
        self.menu.meals = {
            1: Meal("Chinese", "Wantang", 12.00),
            2: Meal("Pastries", "Puff pastryoka", 8.00),
            3: Meal("Italian", "Pizza", 12.00),
            4: Meal("ChefSpecials", "Chef's salad", 25.00),
            5: Meal("ChefSpecials", "Chef's plato", 25.00)
        }
        self.menu.available_meals = set(self.menu.meals.keys()) 

        return "Meal value error."

    @patch('builtins.print')
    def test_display_menu(self, mock_print):
        self.menu.display_menu()
        calls = [call("MENU:"), call("-------")]
        calls.extend(call(f"{meal_id}. {meal.name} - ${meal.price}") for meal_id, meal in self.menu.meals.items())
        mock_print.assert_has_calls(calls)

    @patch('builtins.input', side_effect=['1', '2', 'q'])
    @patch('quantity_validator.QuantityValidator.is_valid_quantity', return_value=True)
    def test_select_meals(self, mock_is_valid_quantity, mock_input):
        selected_meals = self.menu.select_meals()
        self.assertEqual(selected_meals, [(1, 2)])

    @patch('builtins.input', side_effect=['6', 'q'])
    def test_select_meals_invalid_meal(self, mock_input):
        with self.assertRaises(InvalidMealError):
            self.menu.select_meals()

    @patch('builtins.input', side_effect=['1', 'ten', 'q'])
    @patch('quantity_validator.QuantityValidator.is_valid_quantity', return_value=False)
    def test_select_meals_invalid_quantity(self, mock_is_valid_quantity, mock_input):
        with self.assertRaises(InvalidQuantityError):
            self.menu.select_meals()

if __name__ == "__main__":
    unittest.main()
