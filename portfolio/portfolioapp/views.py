from django.views.generic import ListView

from .models import PortfolioProject


class PortfolioProjectListView(ListView):
    model = PortfolioProject
