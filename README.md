# shop

Tiny order-pricing library used to try out automated PR review.

```bash
python -m unittest discover -s tests -t .
```

## Stock and webhooks

- `shop.inventory`: stock levels with reservations (reserve on checkout, release on cancel) and SKU search.
- `shop.webhooks`: signed outgoing notifications to customer-configured URLs, and signature checks for incoming ones.
