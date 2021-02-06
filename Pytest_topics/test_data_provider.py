import pytest
from Pytest_topics.utils.util import get_data

@pytest.mark.parametrize("a,b,c,d", get_data())
def test_checkdata_from_file(a,b,c,d):
    print (d)