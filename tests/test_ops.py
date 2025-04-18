from src.math_ops import add, sub, mul

def test_add():
    assert add(2, 3) == 5
    assert add(-2, 2) == 0
    assert add(5, 2) == 7

def test_sub():
    assert sub(5, 2) == 3
    assert sub(5, 15) == -10
    assert sub(5, 5) == 0
    assert sub(5, 1) == 4

def test_mul():
    assert mul(5, 2) == 10
    assert mul(5, 15) == 75
    assert mul(5, -5) == -25