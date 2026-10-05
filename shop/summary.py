from shop.models import Order
from shop.pricing import order_total
from shop.tax import vat_amount


def order_summary(order: Order, country: str) -> dict[str, str]:
    """Net, VAT and gross totals of an order, formatted as strings with two decimals."""
    net = order_total(order)
    vat = vat_amount(net, country)
    return {
        "items": str(sum(item.quantity for item in order.items)),
        "net": f"{net:.2f}",
        "vat": f"{vat:.2f}",
        "gross": f"{net + vat:.2f}",
    }
