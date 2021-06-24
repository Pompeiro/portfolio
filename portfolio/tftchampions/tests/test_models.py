import pytest

pytestmark = pytest.mark.django_db


def test___str__(champion):
    assert champion.__str__() == champion.name
    assert str(champion) == champion.name


def test_get_absolute_url(champion):
    url = champion.get_absolute_url()

    assert url == f"/tftchampions/{champion.slug}/"
