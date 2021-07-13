from django.urls import path

from . import views

app_name = "charts"
urlpatterns = [
    path(
        route="",
        view=views.ChartsListView.as_view(),
        name="list",
    ),
    path(
        route="form/",
        view=views.ChartsFormView.as_view(),
        name="form",
    ),
    path(
        route="<slug:slug>/",
        view=views.ChartsDetailView.as_view(),
        name="detail",
    ),
]
