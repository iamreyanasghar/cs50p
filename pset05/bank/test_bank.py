from bank import value

''' Testing value() form bank.py '''

def test_hello():
    assert value("hello") == 0
    assert value("Hello") == 0
    assert value("HELLO") == 0

def test_h():
    assert value("Hi") == 20
    assert value("hi") == 20



def test_other():
    assert value("Good morning") == 100
    assert value("Good Morning") == 100
    assert value("good morning") == 100
    assert value("GOOD MORNING") == 100
