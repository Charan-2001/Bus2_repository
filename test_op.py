import math

def test_sqrt_negative_num():
    num = -25
    assert math.sqrt(num) == ValueError

def test_sqrt_decimal_num():
    num = 7.5
    assert math.sqrt(num) == math.sqrt(7.5)

def test_sqrt_string():
    num = "Hello"
    assert math.sqrt(num) == TypeError
