from jar import Jar
import pytest

def test_init():
    jar = Jar()

    assert str(jar) == ""



def test_str():
    jar = Jar()
    assert str(jar) == ""

    jar.deposit(1)
    assert str(jar) == "🍪"

    jar.deposit(11)
    assert str(jar) == "🍪" * 12


def test_deposit():
    jar = Jar()
    
    jar.deposit(3)
    assert str(jar) == "🍪" * 3

    with pytest.raises(ValueError):
        jar.deposit(15)


def test_withdraw():
    jar = Jar()

    jar.deposit(10)
    jar.withdraw(5)
    
    assert str(jar) == "🍪" * 5

    with pytest.raises(ValueError):
        jar.withdraw(6)

