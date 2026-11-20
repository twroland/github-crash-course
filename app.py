"""Tiny sample app so the template pipeline has something to test."""


def cart_total(prices: list[float], coupon_rate: float = 0.0) -> float:
    """Return the cart total after applying a coupon rate between 0 and 0.5."""
    if not 0.0 <= coupon_rate <= 0.5:
        raise ValueError("coupon_rate must be between 0 and 0.5")
    if any(p < 0 for p in prices):
        raise ValueError("prices must not be negative")
    return round(sum(prices) * (1 - coupon_rate), 2)
