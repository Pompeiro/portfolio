from django.forms.models import ModelForm
from django.forms.widgets import CheckboxSelectMultiple, Select

from ..tftchampions.models import Champion


class ChampionForm(ModelForm):
    class Meta:
        CHOICES = Champion.objects.all()

        model = Champion
        fields = ("name",)
        widgets = {
            "name": Select(choices=((x.id, x.name) for x in CHOICES)),
            "options": CheckboxSelectMultiple(),
        }
