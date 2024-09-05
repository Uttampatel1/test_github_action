from src.math_operations import add, subtract, multiply, divide
import pytest

def test_add():
    assert add(2, 3) == 5
    assert add(-1, 1) == 0
    assert add(0, 0) == 0

def test_subtract():
    assert subtract(5, 3) == 2
    assert subtract(0, 5) == -5
    assert subtract(-5, -3) == -2

def test_multiply():
    assert multiply(4, 5) == 20
    assert multiply(0, 5) == 0
    assert multiply(-4, 5) == -20

def test_divide():
    assert divide(10, 2) == 5
    assert divide(-10, 2) == -5
    with pytest.raises(ValueError, match="Cannot divide by zero"):
        divide(10, 0)
