# shop

Tiny order-pricing library used to try out automated PR review.

```bash
python -m unittest discover -s tests -t .
```

## Loyalty and receipts

- `shop.loyalty`: one point per 10 currency units spent, valid for 12 months; 100 points = 1 unit off.
- `shop.receipts`: plain-text receipts, saved under `receipts/` and printable via CUPS (`lp`).
