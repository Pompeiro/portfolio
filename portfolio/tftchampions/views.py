from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import CreateView, DetailView, ListView

from .models import Champion


class ChampionListView(ListView):
    model = Champion


class ChampionDetailView(DetailView):
    model = Champion


class ChampionCreateView(LoginRequiredMixin, CreateView):
    model = Champion
    fields = [
        "name",
        "dps",
        "attackspeed",
        "dmg",
        "range",
        "hp",
        "mana",
        "armor",
        "mr",
        "origin_prim",
        "origin_sec",
        "class_prim",
        "class_sec",
        "cost",
        "tier",
    ]
