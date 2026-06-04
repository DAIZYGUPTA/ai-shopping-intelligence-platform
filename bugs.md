# Known Bugs

## Bug 1 - Price Extraction

Problem:
Some products return price=0.0.

Example:
Jockey Men Maroon T-shirt

Reason:
Current parser only supports:

span.product-discountedPrice

Need:
Support all Myntra price layouts.

Priority:
High

Status:
Pending