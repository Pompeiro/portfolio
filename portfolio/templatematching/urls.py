from django.urls import path

from . import views

app_name = "templatematching"
urlpatterns = [
    path(
        route="",
        view=views.TemplateMatchingListView.as_view(),
        name="list",
    ),
    path(
        route="add/",
        view=views.TemplateMatchingCreateView.as_view(),
        name="add",
    ),
    path(
        route="<slug:slug>/",
        view=views.TemplateMatchingDetailView.as_view(),
        name="detail",
    ),
]
