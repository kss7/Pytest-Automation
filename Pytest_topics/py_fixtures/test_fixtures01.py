import pytest

@pytest.fixture()
def setup_list():
    print("\n in fixtures.. setup_list.. \n")
    city = ['New York', 'London', 'Riyadh', 'Singapore', 'Mumbai']
    return city

def test_getItem(setup_list):
    #print(setup_list[1:3])
    assert setup_list[0] == 'New York'
    assert setup_list[::2] == ['New York', 'Riyadh', 'Mumbai']

def myReverse(lst):
    lst.reverse()
    return lst

def test_reverseList(setup_list):
    assert setup_list[::-2] == ['Mumbai', 'Riyadh', 'New York']
    assert setup_list[::-1] == myReverse(setup_list)

@pytest.mark.xfail(reason="known issue: usefixtures cannot use the fixture’s return value")
@pytest.mark.usefixtures("setup_list")
def test_usefixturedemo():
    assert 1 == 1
    assert (setup_list[0])