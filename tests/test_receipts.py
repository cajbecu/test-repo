import unittest
from decimal import Decimal

from shop.models import Item, Order
from shop.receipts import render_receipt


class ReceiptsTest(unittest.TestCase):
    def test_render_receipt(self):
        order = Order("c1", [Item("apple", Decimal("1.50"), 2)])
        text = render_receipt(order)
        self.assertIn("apple", text)
        self.assertIn("3.00", text)
