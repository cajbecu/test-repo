import unittest
from decimal import Decimal

from shop.tax import vat_amount, vat_rate


class TaxTest(unittest.TestCase):
    def test_rate_is_case_and_space_insensitive(self):
        self.assertEqual(vat_rate(" de "), Decimal("19"))

    def test_unknown_country(self):
        with self.assertRaises(ValueError):
            vat_rate("XX")

    def test_vat_amount_rounds_half_up(self):
        # 0.05 * 21% = 0.0105 -> 0.01
        self.assertEqual(vat_amount(Decimal("0.05"), "RO"), Decimal("0.01"))
        # 0.50 * 19% = 0.095 -> 0.10
        self.assertEqual(vat_amount(Decimal("0.50"), "DE"), Decimal("0.10"))

    def test_zero_rate(self):
        self.assertEqual(vat_amount(Decimal("99.99"), "US"), Decimal("0.00"))
