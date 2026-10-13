import unittest
from decimal import Decimal

from shop.models import Item, Order
from shop.promotions import bulk_percent, discounted_total


class PromotionsTest(unittest.TestCase):
    def test_no_bulk_discount_for_small_orders(self):
        self.assertEqual(bulk_percent(3), Decimal("0"))

    def test_big_order_gets_discount(self):
        self.assertEqual(bulk_percent(60), Decimal("15"))

    def test_discounted_total(self):
        order = Order("c1", [Item("a", Decimal("10.00"), 2)])
        self.assertEqual(discounted_total(order), Decimal("20.00"))
