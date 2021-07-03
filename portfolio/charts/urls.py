from django.urls import path

from . import views

app_name = "charts"
urlpatterns = [
    path(
        route="",
        view=views.ChampionListView.as_view(),
        name="list",
    ),
    path(
        route="form/",
        view=views.ChampionFormView.as_view(),
        name="form",
    ),
    path(
        route="<slug:slug>/",
        view=views.ChartDetailView.as_view(),
        name="detail",
    ),
]
