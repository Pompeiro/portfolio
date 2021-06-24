from django.views.generic import DetailView, ListView

from .models import Champion


class ChampionListView(ListView):
    model = Champion


class ChampionDetailView(DetailView):
    model = Champion
