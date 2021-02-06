import pytest
import sys

def test_strjoin():
    s1 = 'Python,Pytest and Automation'
    l1 = ['Python,Pytest', 'and', 'Automation']
    l2 = ['Python', 'Pytest and Automation']
    assert ' '.join(l1) == s1

@pytest.mark.xfail(raises=IndexError, reason="known issue")
def test_str04():
    letters = 'abcdefghijklmnopqrstuvwxyz'
    assert letters[10]

@pytest.mark.xfail(sys.platform=='win32', reason="works only in win32")
def test_str05():
    letters = 'abcd'
    num = 1234
    assert letters + num == 'abcd1234'