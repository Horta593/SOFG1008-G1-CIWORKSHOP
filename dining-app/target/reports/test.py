import unittest

 
def test_quantity(self):
    assert self.calculate_cost() < 0, "Should be greater than zero."

def test_cost_calculation(self):
    assert self.quantity < 5, "Do not apply discount!"
    assert self.quantity >= 5 and self.quantity < 9, self.total_cost * 0.10
    assert self.quantity >= 10, self.total_cost * 0.20

def test_special_offer_discount(self):
    assert self.total_cost < 50, "Do not apply discount!"
    assert self.total_cost >= 50 and self.total_cost < 99, self.total_cost - 10
    assert self.total_cost >= 100, self.total_cost - 25


if __name__ == "__main__":
    test_quantity()
    test_cost_calculation()
    print("Everything passed")