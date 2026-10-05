from decimal import ROUND_HALF_UP, Decimal

CENT = Decimal("0.01")

# Standard VAT rates, in percent.
VAT_RATES: dict[str, Decimal] = {
    "DE": Decimal("19"),
    "FR": Decimal("20"),
    "IE": Decimal("23"),
    "RO": Decimal("21"),
    "US": Decimal("0"),
}


def vat_rate(country: str) -> Decimal:
    """Standard VAT rate for an ISO 3166-1 alpha-2 country code."""
    try:
        return VAT_RATES[country.strip().upper()]
    except KeyError:
        raise ValueError(f"no VAT rate configured for country {country!r}") from None


def vat_amount(net: Decimal, country: str) -> Decimal:
    """VAT due on a net amount, rounded to cents."""
    return (net * vat_rate(country) / Decimal("100")).quantize(CENT, rounding=ROUND_HALF_UP)
