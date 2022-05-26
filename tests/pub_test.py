import unittest

from src.customer import Customer
from src.drink import Drink
from src.pub import Pub

class TestPub(unittest.TestCase):

    def setUp(self):
        self.pub = Pub("The Prancing Pony", 100, {Drink("Beer", 4), Drink("Wine", 3), Drink("Bourbon", 2)})
        self.beer = Drink("Beer", 4)
        self.customer = Customer("James", 100)

    def test_pub_has_name(self):
        self.assertEqual("The Prancing Pony", self.pub.name)

    def test_pub_has_till(self):
        self.assertEqual(100, self.pub.till)

    def test_increase_till(self):
        self.pub.increase_till(50)
        self.assertEqual(150, self.pub.till)

    def test_sell_a_beer(self):
        self.pub.sell_a_drink(self.beer)
        self.pub.increase_till(self.beer.price)
        self.assertEqual(104, self.pub.till)
        self.assertEqual(96, self.customer.wallet)