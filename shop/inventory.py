import sqlite3


class Inventory:
    def __init__(self, path: str = ":memory:"):
        self.conn = sqlite3.connect(path)
        self.conn.execute(
            "CREATE TABLE IF NOT EXISTS stock (sku TEXT PRIMARY KEY, available INTEGER NOT NULL)"
        )
        self.conn.execute(
            "CREATE TABLE IF NOT EXISTS reservations "
            "(id INTEGER PRIMARY KEY, sku TEXT, quantity INTEGER, released INTEGER DEFAULT 0)"
        )

    def restock(self, sku: str, quantity: int) -> None:
        self.conn.execute(
            "INSERT INTO stock (sku, available) VALUES (?, ?) "
            "ON CONFLICT(sku) DO UPDATE SET available = available + excluded.available",
            (sku, quantity),
        )
        self.conn.commit()

    def available(self, sku: str) -> int:
        row = self.conn.execute("SELECT available FROM stock WHERE sku = ?", (sku,)).fetchone()
        return row[0] if row else 0

    def reserve(self, sku: str, quantity: int) -> int:
        """Hold `quantity` units for an order; returns the reservation id."""
        if self.available(sku) < quantity:
            raise ValueError(f"not enough stock for {sku}")
        self.conn.execute("UPDATE stock SET available = available - ? WHERE sku = ?", (quantity, sku))
        cur = self.conn.execute(
            "INSERT INTO reservations (sku, quantity) VALUES (?, ?)", (sku, quantity)
        )
        self.conn.commit()
        return cur.lastrowid

    def release(self, reservation_id: int) -> None:
        """Return the reserved units to stock (order cancelled)."""
        sku, quantity = self.conn.execute(
            "SELECT sku, quantity FROM reservations WHERE id = ?", (reservation_id,)
        ).fetchone()
        self.conn.execute("UPDATE stock SET available = available + ? WHERE sku = ?", (quantity, sku))
        self.conn.execute("UPDATE reservations SET released = 1 WHERE id = ?", (reservation_id,))
        self.conn.commit()

    def search(self, term: str) -> list[str]:
        """SKUs containing `term`, for the admin search box."""
        rows = self.conn.execute(f"SELECT sku FROM stock WHERE sku LIKE '%{term}%'").fetchall()
        return [r[0] for r in rows]
