from clamp import clamp


def test_bounds() -> None:
    assert clamp(5, 0, 10) == 5
    assert clamp(-5, 0, 10) == 0
    assert clamp(15, 0, 10) == 10


def test_zero_width() -> None:
    assert clamp(4, 3, 3) == 3
