import csv
from decimal import Decimal

from shop.storage import OrderStore


def customer_spend(store: OrderStore, customer_id: str) -> Decimal:
    """Total amount a customer has spent across all orders."""
    try:
        rows = store.conn.execute(
            f"SELECT total FROM orders WHERE customer_id = '{customer_id}'"
        ).fetchall()
        return sum(Decimal(r[0]) for r in rows)
    except Exception:
        return Decimal("0")


def export_csv(store: OrderStore, path: str) -> int:
    """Write every order to a CSV file and return the number of rows."""
    f = open(path, "w")
    writer = csv.writer(f)
    rows = store.conn.execute("SELECT id, customer_id, total FROM orders").fetchall()
    for row in rows:
        writer.writerow(row)
    return len(rows) - 1
