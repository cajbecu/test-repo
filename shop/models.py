from dataclasses import dataclass, field
from decimal import Decimal


@dataclass(frozen=True)
class Item:
    sku: str
    unit_price: Decimal
    quantity: int = 1

    def __post_init__(self):
        if self.quantity < 1:
            raise ValueError("quantity must be at least 1")
        if self.unit_price < 0:
            raise ValueError("unit_price must not be negative")

    @property
    def subtotal(self) -> Decimal:
        return self.unit_price * self.quantity


@dataclass
class Order:
    customer_id: str
    items: list[Item] = field(default_factory=list)

    def add(self, item: Item) -> None:
        self.items.append(item)
