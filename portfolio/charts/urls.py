from django.urls import path

from . import views

app_name = "charts"
urlpatterns = [
    path(
        route="<slug:slug>/",
        view=views.ChartDetailView.as_view(),
        name="detail",
    ),
]
