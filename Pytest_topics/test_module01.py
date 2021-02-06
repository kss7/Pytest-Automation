
def test_a1():
    assert 5 + 5 == 10
    assert 5 - 5 == 0
    assert 5 * 5 == 25
    assert 5 / 5 == 1

#this is a failed test
def test_a2():
    assert 9/5 == 1.5, "failed test intentionally"

#test no.3
def test_a3():
    assert 9//5 == 1 #integer truncating division