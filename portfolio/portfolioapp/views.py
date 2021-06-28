from django.contrib.auth.mixins import UserPassesTestMixin
from django.views.generic import CreateView, DetailView, ListView, UpdateView

from .models import PortfolioProject


class PortfolioProjectListView(ListView):
    model = PortfolioProject


class PortfolioProjectDetailView(DetailView):
    model = PortfolioProject


class PortfolioProjectCreateView(UserPassesTestMixin, CreateView):
    model = PortfolioProject
    fields = ["title", "description", "website", "try_online_url", "photo"]

    # https://stackoverflow.com/questions/58217055/how-can-i-restrict-access-to-a-view-to-only-super-users-in-django
    def test_func(self):
        return self.request.user.is_superuser


class PortfolioProjectUpdateView(UserPassesTestMixin, UpdateView):
    model = PortfolioProject
    fields = ["title", "description", "website", "try_online_url", "photo"]
    action = "Update"

    def test_func(self):
        return self.request.user.is_superuser
