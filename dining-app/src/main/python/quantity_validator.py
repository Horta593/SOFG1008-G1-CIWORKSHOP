class QuantityValidator:
    @staticmethod
    def is_valid_quantity(quantity_str):
        try:
            quantity = int(quantity_str)
            return 1 <= quantity <= 100
        except ValueError:
            return False