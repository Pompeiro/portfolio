from django.views.generic import DetailView

from ..tftchampions.models import Champion


class ChartDetailView(DetailView):
    model = Champion
    template_name = "charts/chart_detail.html"
