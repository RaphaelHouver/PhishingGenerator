from django import forms
from .models import Entreprise

class EntrepriseForm(forms.Form):
    entreprise = forms.ModelChoiceField(
        queryset=Entreprise.objects.all(),
        label="Entreprise",
        required=True,
        widget=forms.Select(attrs={'class': 'form-control'}),
        empty_label="Sélectionnez une entreprise"
    )