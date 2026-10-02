import unittest
from decimal import Decimal

from shop.report import customer_spend
from shop.storage import OrderStore


class ReportTest(unittest.TestCase):
    def test_customer_spend(self):
        store = OrderStore()
        store.save("c1", Decimal("10.50"))
        store.save("c1", Decimal("4.50"))
        self.assertEqual(customer_spend(store, "c1"), Decimal("15.00"))
