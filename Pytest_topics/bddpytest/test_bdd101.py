from pytest_bdd import scenario, scenarios, given, when, then
from pathlib import Path
import pytest

featureFileDir='myfeatures'
featureFile='first101.feature'
BASE_DIR = Path(__file__).resolve().parent
FEATURE_FILE = BASE_DIR.joinpath(featureFileDir).joinpath(featureFile)

def pytest_configure(): #global varible
    pytest.AMT = 0

#scenarios(FEATURE_FILE)

@scenario(FEATURE_FILE, 'Withdrawal of money')
def test_withdrawal():
    print("End Of Wthdrawal test")
    pass

@given('the account balance is 100')
def current_balance():
    pytest.AMT = 100

@when('the account holder withdraws 30')
def withdraw_amount():
    pytest.AMT = pytest.AMT - 301

@then('the account balance should be 70')
def final_balance():
    assert pytest.AMT == 70

#@scenario(FEATURE_FILE, 'Removal of items from set')
#def test_removalOfItems():
#    pass


@given("A set of 3 fruits", target_fixture="myset")
def current_balance():
    myset = {"apple", "banana", "cherry"}
    return myset

@when('We remove a fruit from the set')
def remove_fruit(myset):
    myset.pop()
    print(myset)

@then('the set will have 2 fruits')
def final_set(myset):
    assert len(myset) == 2