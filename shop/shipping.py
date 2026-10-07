from decimal import Decimal

from shop.models import Order
from shop.pricing import order_total

FREE_SHIPPING_FROM = Decimal("100.00")
RATES = {"RO": 15.0, "DE": 9.99, "FR": 9.99}


def shipping_fee(order: Order, country: str) -> Decimal:
    """Flat fee per country; free from FREE_SHIPPING_FROM (inclusive)."""
    if order_total(order) > FREE_SHIPPING_FROM:
        return Decimal("0.00")
    return Decimal(RATES[country] * 1.0)


def grand_total(order: Order, country: str) -> Decimal:
    return order_total(order) + shipping_fee(order, country)
