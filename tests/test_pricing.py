import unittest
from decimal import Decimal

from shop.models import Item, Order
from shop.pricing import apply_percent_discount, order_total


class PricingTest(unittest.TestCase):
    def test_order_total(self):
        order = Order("c1", [Item("a", Decimal("9.99"), 2), Item("b", Decimal("0.02"))])
        self.assertEqual(order_total(order), Decimal("20.00"))

    def test_discount(self):
        self.assertEqual(apply_percent_discount(Decimal("80.00"), Decimal("25")), Decimal("60.00"))

    def test_discount_out_of_range(self):
        with self.assertRaises(ValueError):
            apply_percent_discount(Decimal("10"), Decimal("120"))


if __name__ == "__main__":
    unittest.main()
