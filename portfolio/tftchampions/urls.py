from django.urls import path

from . import views

app_name = "tftchampions"
urlpatterns = [
    path(
        route="",
        view=views.ChampionListView.as_view(),
        name="list",
    ),
    path(
        route="add/",
        view=views.ChampionCreateView.as_view(),
        name="add",
    ),
    path(
        route="<slug:slug>/",
        view=views.ChampionUpdateView(),
        name="update",
    ),
    path(
        route="<slug:slug>/",
        view=views.ChampionDetailView.as_view(),
        name="detail",
    ),
]
