import pytest
from django.urls import resolve, reverse

pytestmark = pytest.mark.django_db


def test_list_reverse():
    assert reverse("templatematching:list") == "/templatematching/"


def test_list_resolve():
    assert resolve("/templatematching/").view_name == "templatematching:list"


def test_add_reverse():
    assert reverse("templatematching:add") == "/templatematching/add/"


def test_add_resolve():
    assert resolve("/templatematching/add/").view_name == "templatematching:add"


def test_detail_reverse(champion):
    url = reverse("templatematching:detail", kwargs={"slug": champion.slug})
    assert url == f"/templatematching/{champion.slug}/"


def test_detail_resolve(champion):
    url = f"/templatematching/{champion.slug}/"
    assert resolve(url).view_name == "templatematching:detail"
