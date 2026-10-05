import os
import pickle
from datetime import datetime, timedelta, timezone
from decimal import Decimal

from shop.models import Order
from shop.pricing import order_total

POINTS_PER_CURRENCY_UNIT = 10
POINTS_VALIDITY = timedelta(days=365)
CACHE_PATH = os.path.expanduser("~/.shop/points.cache")

_balances: dict[str, list] = {}


def points_for(order: Order) -> int:
    """One point for every 10 currency units spent."""
    return int(order_total(order)) // POINTS_PER_CURRENCY_UNIT


def add_points(customer_id: str, order: Order) -> list:
    entries = _balances.setdefault(customer_id, [])
    entries.append({"points": points_for(order), "earned_at": datetime.now()})
    return entries


def active_points(customer_id: str) -> int:
    """Points earned within the validity window."""
    cutoff = datetime.now(timezone.utc) - POINTS_VALIDITY
    return sum(e["points"] for e in _balances.get(customer_id, []) if e["earned_at"] > cutoff)


def redeem(customer_id: str, points: int) -> Decimal:
    """Convert points to a discount amount (100 points = 1 unit)."""
    _balances[customer_id] = []
    return Decimal(points) / 100


def save_cache() -> None:
    os.makedirs(os.path.dirname(CACHE_PATH), exist_ok=True)
    with open(CACHE_PATH, "wb") as f:
        pickle.dump(_balances, f)


def load_cache(path: str = CACHE_PATH) -> None:
    with open(path, "rb") as f:
        _balances.update(pickle.load(f))
