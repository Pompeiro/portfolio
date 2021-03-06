# https://stackoverflow.com/questions/54828495/how-to-do-math-operations-in-django-template
from decimal import Decimal

from django.db.models import ExpressionWrapper, F, FloatField, Max
from django.http import HttpResponseRedirect
from django.urls import reverse
from django.views.generic import DetailView, FormView, ListView

from ..tftchampions.models import Champion
from .forms import ChartForm


class ChartsListView(ListView):
    model = Champion
    template_name = "charts/chart_list.html"

    def get_queryset(self, *args, **kwargs):
        # https://stackoverflow.com/questions/60257540/get-maximum-value-of-a-field-in-django
        max_dps = Champion.objects.aggregate(Max("dps")).get("dps__max")
        max_attackspeed = Champion.objects.aggregate(Max("attackspeed")).get(
            "attackspeed__max"
        )
        max_dmg = Champion.objects.aggregate(Max("dmg")).get("dmg__max")
        max_range = Champion.objects.aggregate(Max("range")).get("range__max")
        max_hp = Champion.objects.aggregate(Max("hp")).get("hp__max")
        max_mana = Champion.objects.aggregate(Max("mana")).get("mana__max")
        max_armor = Champion.objects.aggregate(Max("armor")).get("armor__max")
        max_mr = Champion.objects.aggregate(Max("mr")).get("mr__max")
        max_cost = Champion.objects.aggregate(Max("cost")).get("cost__max")
        max_tier = Champion.objects.aggregate(Max("tier")).get("tier__max")

        # https://stackoverflow.com/questions/54828495/how-to-do-math-operations-in-django-template

        qset = super(ChartsListView, self).get_queryset(*args, **kwargs)
        return qset.annotate(
            scaled_dps=ExpressionWrapper(
                (F("dps") * Decimal("1.0") / max_dps), output_field=FloatField()
            ),
            scaled_attackspeed=ExpressionWrapper(
                (F("attackspeed") * Decimal("1.0") / max_attackspeed),
                output_field=FloatField(),
            ),
            scaled_dmg=ExpressionWrapper(
                (F("dmg") * Decimal("1.0") / max_dmg), output_field=FloatField()
            ),
            scaled_range=ExpressionWrapper(
                (F("range") * Decimal("1.0") / max_range),
                output_field=FloatField(),
            ),
            scaled_hp=ExpressionWrapper(
                (F("hp") * Decimal("1.0") / max_hp), output_field=FloatField()
            ),
            scaled_mana=ExpressionWrapper(
                (F("mana") * Decimal("1.0") / max_mana), output_field=FloatField()
            ),
            scaled_armor=ExpressionWrapper(
                (F("armor") * Decimal("1.0") / max_armor),
                output_field=FloatField(),
            ),
            scaled_mr=ExpressionWrapper(
                (F("mr") * Decimal("1.0") / max_mr), output_field=FloatField()
            ),
            scaled_cost=ExpressionWrapper(
                (F("cost") * Decimal("1.0") / max_cost), output_field=FloatField()
            ),
            scaled_tier=ExpressionWrapper(
                (F("tier") * Decimal("1.0") / max_tier), output_field=FloatField()
            ),
        )

    def get_context_data(self, **kwargs):
        max_dps = Champion.objects.aggregate(Max("dps")).get("dps__max")
        max_attackspeed = Champion.objects.aggregate(Max("attackspeed")).get(
            "attackspeed__max"
        )
        max_dmg = Champion.objects.aggregate(Max("dmg")).get("dmg__max")
        max_range = Champion.objects.aggregate(Max("range")).get("range__max")
        max_hp = Champion.objects.aggregate(Max("hp")).get("hp__max")
        max_mana = Champion.objects.aggregate(Max("mana")).get("mana__max")
        max_armor = Champion.objects.aggregate(Max("armor")).get("armor__max")
        max_mr = Champion.objects.aggregate(Max("mr")).get("mr__max")
        max_cost = Champion.objects.aggregate(Max("cost")).get("cost__max")
        max_tier = Champion.objects.aggregate(Max("tier")).get("tier__max")

        MAX_DICT = {
            "max_dps": max_dps,
            "max_attackspeed": max_attackspeed,
            "max_dmg": max_dmg,
            "max_range": max_range,
            "max_hp": max_hp,
            "max_mana": max_mana,
            "max_armor": max_armor,
            "max_mr": max_mr,
            "max_cost": max_cost,
            "max_tier": max_tier,
        }
        # https://docs.djangoproject.com/en/3.2/ref/class-based-views/mixins-simple/#django.views.generic.base.ContextMixin.extra_context
        # https://newbedev.com/django-passing-variables-to-templates-from-class-based-views
        try:
            Champions = self.request.session["Champions"]

            context = super(ChartsListView, self).get_context_data(**kwargs)
            context.update(MAX_DICT)
            context.update({"Champions": Champions})
            return context

        except (KeyError):
            context = super(ChartsListView, self).get_context_data(**kwargs)
            context.update(MAX_DICT)
            context.update(
                {
                    "Warning": "To render chart first fill form in {}".format(
                        reverse("charts:form")
                    )
                }
            )

            return context


class ChartsDetailView(DetailView):
    model = Champion
    template_name = "charts/chart_detail.html"


class ChartsFormView(FormView):
    form_class = ChartForm
    template_name = "charts/chart_form.html"

    def form_valid(self, form):
        """If the form is valid, redirect to the supplied URL with form results passed in session."""
        Champions = form.cleaned_data.get("Champions")
        self.request.session["Champions"] = Champions
        return HttpResponseRedirect(self.get_success_url())

    def get_success_url(self):
        return reverse("charts:list")
