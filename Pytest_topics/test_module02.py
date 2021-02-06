
class TestMyStuff():
    def test_type(self):
        assert type(1.3) == int

    def test_strs(self):
        assert str.upper('python') == 'PYTHON'
        assert 'pytest'.capitalize() == 'Pytest'