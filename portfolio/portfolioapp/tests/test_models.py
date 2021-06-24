import pytest

pytestmark = pytest.mark.django_db


def test___str__(project):
    assert project.__str__() == project.title
    assert str(project) == project.title


def test_get_absolute_url(project):
    url = project.get_absolute_url()
    assert url == f"/portfolioapp/{project.slug}/"
