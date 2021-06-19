from django.contrib.auth.mixins import UserPassesTestMixin
from django.views.generic import CreateView, DetailView, ListView

from .models import PortfolioProject


class PortfolioProjectListView(ListView):
    model = PortfolioProject


class PortfolioProjectDetailView(DetailView):
    model = PortfolioProject


class PortfolioProjectCreateView(UserPassesTestMixin, CreateView):
    model = PortfolioProject
    fields = ["title", "description", "website", "photo"]

    # https://stackoverflow.com/questions/58217055/how-can-i-restrict-access-to-a-view-to-only-super-users-in-django
    def test_func(self):
        return self.request.user.is_superuser
