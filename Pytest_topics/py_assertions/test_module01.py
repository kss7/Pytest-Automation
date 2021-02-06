
def test_a1():
    assert 4 != 3

def test_a2():
    assert 1

def test_a3():
    assert "abc" == 'abcd'

def test_a4():
    assert ((3-1)*4/2) == 4.0

def test_a5():
    assert 1 in divmod(9,5)
    assert 'put' not in 'this is pytest'
    assert [1,2,4] == [1,2,4]