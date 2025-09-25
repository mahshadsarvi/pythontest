import pytest
from plates import is_valid

def main():
    test_is_valid_0()
    test_is_valid_1()
    test_is_valid_2()
    test_is_valid_3()

def test_is_valid_0():
    assert is_valid('CS50')==True
    assert is_valid('05CS')==False
    assert is_valid('cs50')==True

def test_is_valid_1():
    assert is_valid('CS05')==False
    assert is_valid('CS50P')==False
    assert is_valid('OUTTIME')==False

def test_is_valid_2():
    assert is_valid('PL3.14')==False
    assert is_valid('H')==False

def test_is_valid_3():
    assert is_valid('OUTTI')==True
    assert is_valid('50CS')==False




