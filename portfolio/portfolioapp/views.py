from django.views.generic import CreateView, DetailView, ListView

from .models import PortfolioProject


class PortfolioProjectListView(ListView):
    model = PortfolioProject


class PortfolioProjectDetailView(DetailView):
    model = PortfolioProject


class PortfolioProjectCreateView(CreateView):
    model = PortfolioProject
    fields = ["title", "description", "website", "photo"]
