import pytest
from django.urls import resolve, reverse

pytestmark = pytest.mark.django_db


def test_list_reverse():
    assert reverse("portfolioapp:list") == "/portfolioapp/"


def test_list_resolve():
    assert resolve("/portfolioapp/").view_name == "portfolioapp:list"


def test_add_reverse():
    assert reverse("portfolioapp:add") == "/portfolioapp/add/"


def test_add_resolve():
    assert resolve("/portfolioapp/add/").view_name == "portfolioapp:add"


def test_detail_reverse(project):
    url = reverse("portfolioapp:detail", kwargs={"slug": project.slug})
    assert url == f"/portfolioapp/{project.slug}/"


def test_detail_resolve(project):
    url = f"/portfolioapp/{project.slug}/"
    assert resolve(url).view_name == "portfolioapp:detail"
