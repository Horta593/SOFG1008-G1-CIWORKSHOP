class InvalidQuantityError(Exception):
    def __init__(self):
        super().__init__("Invalid quantity! Please enter a positive integer between 1 and 100.")


class InvalidMealError(Exception):
    def __init__(self):
        super().__init__("One or more selected meals are not available on the menu. Please re-select.")


class InvalidConfirmationError(Exception):
    def __init__(self):
        super().__init__("Invalid input! Please enter 'y' or 'n'.")