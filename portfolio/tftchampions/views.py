from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import CreateView, DetailView, ListView, UpdateView

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

    def form_valid(self, form):
        form.instance.creator = self.request.user
        return super().form_valid(form)


class ChampionUpdateView(LoginRequiredMixin, UpdateView):
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
    action = "Update"
