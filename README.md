# shop

Tiny order-pricing library used to try out automated PR review.

```bash
python -m unittest discover -s tests -t .
```

## VAT

- `shop.tax`: standard VAT rates per country (ISO 3166-1 alpha-2), VAT rounded half-up to cents.
- `shop.summary`: net / VAT / gross totals of an order, as two-decimal strings.
