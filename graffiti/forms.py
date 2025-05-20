from django import forms

from .models import Graffiti


class GraffitiForm(forms.ModelForm):
    class Meta:
        model = Graffiti
        fields = ["svg_data"]
        widgets = {
            "svg_data": forms.HiddenInput(),
        }
