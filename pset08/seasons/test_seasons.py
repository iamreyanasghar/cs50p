from seasons import get_date, convert_to_minutes
from datetime import date, timedelta
import pytest


def test_get_date_valid():
    assert get_date("2000-01-01") == date(2000, 1, 1)


def test_get_date_invalid():
    with pytest.raises(SystemExit):
        get_date("January 1, 2000")


def test_convert_to_minutes():
    birth_date = get_date("2000-01-01")
    assert isinstance(convert_to_minutes(birth_date), str)
