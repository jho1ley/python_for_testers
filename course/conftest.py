from course.model.group import Group
from course.fixture.application import Application
import pytest

@pytest.fixture(scope="session")
def app(request):
    fixture = Application()
    request.addfinalizer(fixture.destroy)
    return fixture
