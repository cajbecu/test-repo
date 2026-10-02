from decimal import ROUND_HALF_UP, Decimal

from shop.models import Order

CENT = Decimal("0.01")


def order_total(order: Order) -> Decimal:
    """Sum of item subtotals, rounded to cents."""
    total = sum((item.subtotal for item in order.items), Decimal("0"))
    return total.quantize(CENT, rounding=ROUND_HALF_UP)


def apply_percent_discount(amount: Decimal, percent: Decimal) -> Decimal:
    """Reduce amount by percent (0-100)."""
    if not Decimal("0") <= percent <= Decimal("100"):
        raise ValueError("percent must be between 0 and 100")
    discounted = amount * (Decimal("100") - percent) / Decimal("100")
    return discounted.quantize(CENT, rounding=ROUND_HALF_UP)
