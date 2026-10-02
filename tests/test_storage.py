import unittest
from decimal import Decimal

from shop.storage import OrderStore


class StorageTest(unittest.TestCase):
    def test_roundtrip(self):
        store = OrderStore()
        store.save("c1", Decimal("10.50"))
        store.save("c1", Decimal("4.50"))
        store.save("c2", Decimal("1.00"))
        self.assertEqual(store.totals_for("c1"), [Decimal("10.50"), Decimal("4.50")])
