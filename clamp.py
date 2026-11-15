"""Clamp helper with an injected reversed-bound bug."""


def clamp(value: int, lower: int, upper: int) -> int:
    return min(lower, max(upper, value))
