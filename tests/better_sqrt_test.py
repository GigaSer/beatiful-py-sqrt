from src.bsqrt import *


def test_better_sqrt():
    assert better_sqrt(-180) == (-6, 5)
    assert better_sqrt(-100) == (-10, 1)
    assert better_sqrt(-70) == (-1, 70)
    assert better_sqrt(-16) == (-4, 1)
    assert better_sqrt(-1) == (-1, 1)
    assert better_sqrt(0) == (0, 0)
    assert better_sqrt(1) == (1, 1)
    assert better_sqrt(16) == (4, 1)
    assert better_sqrt(18) == (3, 2)
    assert better_sqrt(20) == (2, 5)
    assert better_sqrt(72) == (6, 2)
    assert better_sqrt(98) == (7, 2)
