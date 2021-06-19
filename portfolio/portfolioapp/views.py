from django.views.generic import DetailView, ListView

from .models import PortfolioProject


class PortfolioProjectListView(ListView):
    model = PortfolioProject


class PortfolioProjectDetailView(DetailView):
    model = PortfolioProject
