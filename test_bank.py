from bank import value

def test_by_start_hello():
    assert value('hello everyone') == 0

def test_by_start_h():
    assert value('hi everyone') == 20

def test_by_start_else():
    assert value('greeting') == 100

def test_by_start_without_case_insensivity():
    assert value('Hello Everyone') == 0
    assert value('Hi Everyone') == 20
    assert value('Greeting') == 100





