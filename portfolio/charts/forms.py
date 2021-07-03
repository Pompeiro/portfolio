from django import forms

from ..tftchampions.models import Champion


class ChampForm(forms.Form):
    CHOICES = Champion.objects.all()
    OPTIONS = ((x.name, x.name) for x in CHOICES)
    Champions = forms.MultipleChoiceField(
        widget=forms.CheckboxSelectMultiple, choices=OPTIONS
    )
