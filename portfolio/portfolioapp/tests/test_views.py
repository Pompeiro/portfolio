import pytest
from django.urls import reverse
from pytest_django.asserts import assertContains

from ..models import PortfolioProject
from ..views import (
    PortfolioProjectCreateView,
    PortfolioProjectDetailView,
    PortfolioProjectListView,
    PortfolioProjectUpdateView,
)
from .factories import PortfolioProjectFactory

pytestmark = pytest.mark.django_db


def test_good_portfolioproject_list_view(rf):
    url = reverse("portfolioapp:list")
    request = rf.get(url)
    callable_obj = PortfolioProjectListView.as_view()
    response = callable_obj(request)

    assertContains(response, "Project list")


def test_good_portfolioproject_detail_view(rf, project):
    url = reverse("portfolioapp:detail", kwargs={"slug": project.slug})
    request = rf.get(url)
    callable_obj = PortfolioProjectDetailView.as_view()
    response = callable_obj(request, slug=project.slug)

    assertContains(response, project.title)


def test_good_portfolioproject_create_view(rf, admin_user):
    url = reverse("portfolioapp:add")
    request = rf.get(url)
    request.user = admin_user
    callable_obj = PortfolioProjectCreateView.as_view()
    response = callable_obj(request)

    assert response.status_code == 200


def test_portfolioproject_list_contains_2_projects(rf):
    project1 = PortfolioProjectFactory()
    project2 = PortfolioProjectFactory()

    request = rf.get(reverse("portfolioapp:add"))
    response = PortfolioProjectListView.as_view()(request)

    assertContains(response, project1.title)
    assertContains(response, project2.title)


def test_detail_contains_portfolioproject_data(rf, project):
    url = reverse("portfolioapp:detail", kwargs={"slug": project.slug})
    request = rf.get(url)
    callable_obj = PortfolioProjectDetailView.as_view()
    response = callable_obj(request, slug=project.slug)

    assertContains(response, project.title)
    assertContains(response, project.description)
    assertContains(response, project.website)
    assertContains(response, project.photo.url)


def test_portfolioproject_create_form_valid(rf, admin_user, project, photo):
    form_data = {
        "title": "New test project for testcase",
        "description": project.description,
        "website": project.website,
        "photo": photo,
    }

    request = rf.post(reverse("portfolioapp:add"), form_data)
    request.user = admin_user
    PortfolioProjectCreateView.as_view()(request)

    created_project = PortfolioProject.objects.get(
        title="New test project for testcase"
    )

    assert created_project.title == "New test project for testcase"
    assert created_project.description == project.description
    assert created_project.website == project.website
    assert created_project.photo.url == "/media/portfolioapp/small.gif"


def test_portfolioproject_create_correct_title(rf, admin_user):
    """Page title for PortfolioProjectCreateView should be Add Project."""
    request = rf.get(reverse("portfolioapp:add"))
    request.user = admin_user
    response = PortfolioProjectCreateView.as_view()(request)

    assertContains(response, "Add Project")


def test_good_portfolioproject_update_view(rf, admin_user, project):
    url = reverse("portfolioapp:update", kwargs={"slug": project.slug})
    request = rf.get(url)
    request.user = admin_user
    callable_obj = PortfolioProjectUpdateView.as_view()
    response = callable_obj(request, slug=project.slug)

    assertContains(response, "Update Project")


def test_portfolioproject_update(rf, admin_user, project, photo):
    """POST request to PortfolioProjectUpdateView updates a project and redirects."""
    form_data = {
        "title": project.title,
        "description": "Something new",
        "website": project.website,
        "photo": photo,
    }

    url = reverse("portfolioapp:update", kwargs={"slug": project.slug})
    request = rf.post(url, form_data)
    request.user = admin_user
    callable_obj = PortfolioProjectUpdateView.as_view()
    callable_obj(request, slug=project.slug)

    project.refresh_from_db()
    assert project.description == "Something new"
