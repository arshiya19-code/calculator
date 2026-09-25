from calculator import total_with_tax


def test_total_with_tax_adds_tax() -> None:
    assert total_with_tax(100, 0.08) == 108
