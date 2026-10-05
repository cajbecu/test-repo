import unittest

from shop.inventory import Inventory


class InventoryTest(unittest.TestCase):
    def test_reserve_and_release(self):
        inv = Inventory()
        inv.restock("apple", 10)
        rid = inv.reserve("apple", 4)
        self.assertEqual(inv.available("apple"), 6)
        inv.release(rid)
        self.assertEqual(inv.available("apple"), 10)

    def test_reserve_too_much(self):
        inv = Inventory()
        inv.restock("apple", 1)
        with self.assertRaises(ValueError):
            inv.reserve("apple", 2)

    def test_search(self):
        inv = Inventory()
        inv.restock("apple-red", 1)
        inv.restock("pear", 1)
        self.assertEqual(inv.search("apple"), ["apple-red"])
