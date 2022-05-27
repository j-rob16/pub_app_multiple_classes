import unittest

from src.customer import Customer
from src.drink import Drink


class TestCustomer(unittest.TestCase):
    
    def setUp(self):
        self.customer = Customer("James", 100, 20)
        self.drink = Drink("Beer", 4)

    def test_customer_has_name(self):
        self.assertEqual("James", self.customer.name)

    def test_customer_has_money(self):
        self.assertEqual(100, self.customer.wallet)

    def test_customer_pays_for_drink(self):
        self.customer.pay_for_drink(self.drink)
        self.assertEqual(96, self.customer.wallet)

    def test_customer_has_age(self):
        self.assertEqual(20, self.customer.age)

    def test_customer_is_old_enough(self):
        self.assertEqual(True, self.customer.customer_can_buy_alcohol(self))