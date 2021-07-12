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


def test_detail_reverse(uploaded_image):
    url = reverse("templatematching:detail", kwargs={"slug": uploaded_image.slug})
    assert url == f"/templatematching/{uploaded_image.slug}/"


def test_detail_resolve(uploaded_image):
    url = f"/templatematching/{uploaded_image.slug}/"
    assert resolve(url).view_name == "templatematching:detail"
