from django import forms

from ..tftchampions.models import Champion


class ChampForm(forms.Form):
    CHOICES = Champion.objects.all()
    OPTIONS = ((x.name, x.name) for x in CHOICES)
    Champions = forms.MultipleChoiceField(
        widget=forms.CheckboxSelectMultiple, choices=OPTIONS
    )

    def clean_Champions(self):
        value = self.cleaned_data["Champions"]
        if len(value) > 5:
            raise forms.ValidationError("You can't select more than 5 champions.")
        return value
