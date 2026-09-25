"""Checkout operations built on the calculator module."""

from calculator import total_with_tax


def checkout_total(subtotal: float, tax_rate: float) -> float:
    """Return the taxed total used by checkout."""
    return total_with_tax(subtotal, tax_rate)
