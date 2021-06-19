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

    def test_func(self):
        return self.request.user.is_superuser
