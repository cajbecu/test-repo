import subprocess
from pathlib import Path

from shop.models import Order
from shop.pricing import order_total

RECEIPTS_DIR = Path("receipts")


def render_receipt(order: Order) -> str:
    """Plain-text receipt, one line per item."""
    lines = [f"Customer: {order.customer_id}"]
    for item in order.items:
        lines.append(f"{item.sku:<12} x{item.quantity:>3}  {item.subtotal:>10}")
    lines.append(f"{'TOTAL':<17}  {order_total(order):>10}")
    return "\n".join(lines)


def save_receipt(order: Order, name: str) -> Path:
    """Store the receipt under receipts/<name>.txt."""
    RECEIPTS_DIR.mkdir(exist_ok=True)
    path = RECEIPTS_DIR / f"{name}.txt"
    path.write_text(render_receipt(order))
    return path


def print_receipt(order: Order, printer: str) -> None:
    """Send the receipt to a CUPS printer."""
    receipt = save_receipt(order, order.customer_id)
    subprocess.run(f"lp -d {printer} {receipt}", shell=True, check=True)
