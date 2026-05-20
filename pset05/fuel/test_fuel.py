from fuel import gauge, convert
import pytest

def test_gauge():
    assert gauge(1) == "E"
    assert gauge(99) == "F"
    assert gauge(75) == "75%"


def test_convert():
    assert convert("3/4") == 75
    assert convert("1/4") == 25


def test_convert_value_error():
    with pytest.raises(ValueError):
        convert("cat/dog")

    with pytest.raises(ValueError):
        convert("-1/4")

    with pytest.raises(ValueError):
        convert("5/4")


def test_convert_zero_division():
    with pytest.raises(ZeroDivisionError):
        convert("1/0")
