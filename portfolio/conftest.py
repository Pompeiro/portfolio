import pytest
from django.core.files.uploadedfile import SimpleUploadedFile

from portfolio.portfolioapp.tests.factories import PortfolioProjectFactory
from portfolio.users.models import User
from portfolio.users.tests.factories import UserFactory


@pytest.fixture(autouse=True)
def media_storage(settings, tmpdir):
    settings.MEDIA_ROOT = tmpdir.strpath


@pytest.fixture
def user() -> User:
    return UserFactory()


@pytest.fixture(name="project")
def fixture_project():
    return PortfolioProjectFactory()


@pytest.fixture(name="photo")
def fixture_photo():
    # https://stackoverflow.com/a/50453780
    # https://stackoverflow.com/questions/26298821/django-testing-model-with-imagefield
    testfile = (
        b"\x47\x49\x46\x38\x39\x61\x01\x00\x01\x00\x00\x00\x00\x21\xf9\x04"
        b"\x01\x0a\x00\x01\x00\x2c\x00\x00\x00\x00\x01\x00\x01\x00\x00\x02"
        b"\x02\x4c\x01\x00\x3b"
    )

    photo = SimpleUploadedFile("small.gif", testfile, content_type="image/gif")
    return photo
