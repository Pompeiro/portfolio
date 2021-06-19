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
        route="<slug:slug>/",
        view=views.PortfolioProjectDetailView.as_view(),
        name="detail",
    ),
]
