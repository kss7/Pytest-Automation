import pytest

def test_delItem(setup01):
    del setup01[-1]
    print(setup01)
    assert setup01 == pytest.weekdays1

def test_removeItem(setup02):
    print(setup02)
    setup02.remove('thur')
    assert setup02 == pytest.weekdays2
