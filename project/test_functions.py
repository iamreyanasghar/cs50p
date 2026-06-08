import pytest
from operations import add, view, remove, tasks
from unittest.mock import patch


# Reset tasks before each test
@pytest.fixture
def reset_tasks():
    tasks.clear()
    yield
    tasks.clear()

def test_add(reset_tasks):
    with patch('builtins.input', return_value="Buy milk"):
        add()
    assert tasks == ["Buy Milk"]

def test_view(reset_tasks):
    tasks.extend(["Buy Milk", "Walk dog"])
    result = view()
    assert "1  Buy Milk" in result
    assert "2  Walk dog" in result

def test_remove_existing(reset_tasks):
    tasks.append("Buy Milk")
    with patch('builtins.input', return_value="Buy Milk"):
        remove()
    assert tasks == []

def test_remove_not_existing(reset_tasks):
    tasks.append("Buy Milk")
    with patch('builtins.input', return_value="Walk dog"):
        result = remove()
    assert result == "Please select or enter the appropriate task for removal."
    assert tasks == ["Buy Milk"]