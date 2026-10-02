import sqlite3
from decimal import Decimal


class OrderStore:
    def __init__(self, path: str = ":memory:"):
        self.conn = sqlite3.connect(path)
        self.conn.execute(
            "CREATE TABLE IF NOT EXISTS orders (id INTEGER PRIMARY KEY, customer_id TEXT, total TEXT)"
        )

    def save(self, customer_id: str, total: Decimal) -> int:
        cur = self.conn.execute(
            "INSERT INTO orders (customer_id, total) VALUES (?, ?)", (customer_id, str(total))
        )
        self.conn.commit()
        return cur.lastrowid

    def totals_for(self, customer_id: str) -> list[Decimal]:
        rows = self.conn.execute(
            "SELECT total FROM orders WHERE customer_id = ? ORDER BY id", (customer_id,)
        ).fetchall()
        return [Decimal(r[0]) for r in rows]
