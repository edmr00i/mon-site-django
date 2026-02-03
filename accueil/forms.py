from django import forms
from .models import Tache


class NomForm(forms.Form):
    nom = forms.CharField(label="Votre nom", max_length=100)


class TacheForm(forms.ModelForm):
    class Meta:
        model = Tache
        fields = ['titre', 'terminee']