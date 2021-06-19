import pytest

from .factories import PortfolioProjectFactory

pytestmark = pytest.mark.django_db


def test___str__():
    project = PortfolioProjectFactory()
    assert project.__str__() == project.title
    assert str(project) == project.title
