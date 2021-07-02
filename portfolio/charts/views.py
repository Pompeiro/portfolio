# https://stackoverflow.com/questions/54828495/how-to-do-math-operations-in-django-template
from django.db.models import F, Max
from django.views.generic import DetailView, ListView

from ..tftchampions.models import Champion


class ChampionListView(ListView):
    model = Champion
    template_name = "charts/chart_list.html"
    # https://stackoverflow.com/questions/60257540/get-maximum-value-of-a-field-in-django
    max_hp = Champion.objects.aggregate(Max("hp")).get("hp__max")

    def get_queryset(self, *args, **kwargs):
        # https://stackoverflow.com/questions/54828495/how-to-do-math-operations-in-django-template

        qset = super(ChampionListView, self).get_queryset(*args, **kwargs)
        return qset.annotate(difference=F("hp") / 100)

    def get_context_data(self, **kwargs):
        # https://docs.djangoproject.com/en/3.2/ref/class-based-views/mixins-simple/#django.views.generic.base.ContextMixin.extra_context
        # https://newbedev.com/django-passing-variables-to-templates-from-class-based-views

        context = super(ChampionListView, self).get_context_data(**kwargs)
        context.update({"max_hp": self.max_hp})
        return context


class ChartDetailView(DetailView):
    model = Champion
    template_name = "charts/chart_detail.html"
