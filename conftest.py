import pytest
from Application import *

@pytest.fixture#(scope="session")
def app(request):
    fixture = Application()
    request.addfinalizer(fixture.finish)
    return fixture
