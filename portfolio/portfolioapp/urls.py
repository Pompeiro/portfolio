from django.urls import path

from . import views

app_name = "portfolioapp"
urlpatterns = [
    path(
        route="",
        view=views.PortfolioProjectListView.as_view(),
        name="list",
    )
]
