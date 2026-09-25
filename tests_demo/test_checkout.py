from checkout import checkout_total


def test_checkout_total_uses_taxed_total() -> None:
    assert checkout_total(200, 0.05) == 210
