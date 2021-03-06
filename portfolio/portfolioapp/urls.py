from django.urls import path

from . import views

app_name = "portfolioapp"
urlpatterns = [
    path(
        route="",
        view=views.PortfolioProjectListView.as_view(),
        name="list",
    ),
    path(
        route="add/",
        view=views.PortfolioProjectCreateView.as_view(),
        name="add",
    ),
    path(
        route="<slug:slug>/update/",
        view=views.PortfolioProjectUpdateView.as_view(),
        name="update",
    ),
    path(
        route="<slug:slug>/",
        view=views.PortfolioProjectDetailView.as_view(),
        name="detail",
    ),
]
