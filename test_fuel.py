import pytest
from fuel import convert , gauge

def test_convert():
    assert convert("4/5") == 80
    assert convert("5/10") == 50
    assert convert("54/100") == 54

def test_gauge():
    assert gauge(80) == "80%"
    assert gauge(99) == "F"
    assert gauge(1) == "E"

def test_zero_division_error():
    with pytest.raises(ZeroDivisionError):
        convert('5/0')

def test_value_error():
    with pytest.raises(ValueError):
        convert("7/3")

