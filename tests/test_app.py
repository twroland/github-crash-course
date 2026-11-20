import pytest

from app import cart_total


def test_total_without_coupon():
    assert cart_total([100, 50]) == 150


def test_total_with_coupon():
    assert cart_total([100, 100], coupon_rate=0.1) == 180


def test_rejects_negative_price():
    # Abuse case: a negative quantity/price must not lower the total.
    with pytest.raises(ValueError):
        cart_total([100, -80])


def test_rejects_excessive_coupon():
    with pytest.raises(ValueError):
        cart_total([100], coupon_rate=0.9)
