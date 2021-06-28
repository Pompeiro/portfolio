import pytest
from django.urls import resolve, reverse

pytestmark = pytest.mark.django_db


def test_list_reverse():
    assert reverse("tftchampions:list") == "/tftchampions/"


def test_list_resolve():
    assert resolve("/tftchampions/").view_name == "tftchampions:list"


def test_add_reverse():
    assert reverse("tftchampions:add") == "/tftchampions/add/"


def test_add_resolve():
    assert resolve("/tftchampions/add/").view_name == "tftchampions:add"


def test_detail_reverse(champion):
    url = reverse("tftchampions:detail", kwargs={"slug": champion.slug})
    assert url == f"/tftchampions/{champion.slug}/"


def test_detail_resolve(champion):
    url = f"/tftchampions/{champion.slug}/"
    assert resolve(url).view_name == "tftchampions:detail"


def test_update_reverse(champion):
    url = reverse("tftchampions:update", kwargs={"slug": champion.slug})
    assert url == f"/tftchampions/{champion.slug}/update/"


def test_update_resolve(champion):
    url = f"/tftchampions/{champion.slug}/update/"
    assert resolve(url).view_name == "tftchampions:update"
