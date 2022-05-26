import unittest

from src.drink import Drink

class TestDrink(unittest.TestCase):

    def setUp(self):
        self.drink = Drink("Beer", 4)

    def test_drink_has_name(self):
        self.assertEqual("Beer", self.drink.name)

    def test_drink_has_price(self):
        self.assertEqual(4, self.drink.price)