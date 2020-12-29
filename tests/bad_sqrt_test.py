from src.bsqrt import *


def test_bad_sqrt():
    assert bad_sqrt(-6, 5) == -180
    assert bad_sqrt(-10, 1) == -100
    assert bad_sqrt(-1, 70) == -70
    assert bad_sqrt(-4, 1) == -16
    assert bad_sqrt(-1, 1) == -1
    assert bad_sqrt(0, 0) == 0
    assert bad_sqrt(0, 1) == 0
    assert bad_sqrt(1, 0) == 0
    assert bad_sqrt(1, 1) == 1
    assert bad_sqrt(4, 1) == 16
    assert bad_sqrt(3, 2) == 18
    assert bad_sqrt(2, 5) == 20
    assert bad_sqrt(6, 2) == 72
    assert bad_sqrt(7, 2) == 98
