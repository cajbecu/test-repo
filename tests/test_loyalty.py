import unittest
from decimal import Decimal

from shop.loyalty import points_for, redeem
from shop.models import Item, Order


class LoyaltyTest(unittest.TestCase):
    def test_points_for(self):
        order = Order("c1", [Item("a", Decimal("25.00"), 2)])
        self.assertEqual(points_for(order), 5)

    def test_redeem(self):
        self.assertEqual(redeem("c1", 250), Decimal("2.5"))
