import unittest
from decimal import Decimal

from shop.models import Item, Order
from shop.summary import order_summary


class SummaryTest(unittest.TestCase):
    def test_summary(self):
        order = Order("c1", [Item("a", Decimal("10.00"), 2), Item("b", Decimal("5.00"))])
        self.assertEqual(
            order_summary(order, "FR"),
            {"items": "3", "net": "25.00", "vat": "5.00", "gross": "30.00"},
        )

    def test_empty_order(self):
        self.assertEqual(
            order_summary(Order("c1"), "DE"),
            {"items": "0", "net": "0.00", "vat": "0.00", "gross": "0.00"},
        )
