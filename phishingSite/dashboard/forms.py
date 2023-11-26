from django import forms
from .models import Entreprise, Template

class CampaignForm(forms.Form):
    entreprise = forms.ModelChoiceField(
        queryset=Entreprise.objects.all(),
        label="Entreprise",
        required=True,
        widget=forms.Select(attrs={'class': 'form-control'}),
        empty_label="Sélectionnez une entreprise"
    )
    template = forms.ModelChoiceField(
        queryset=Template.objects.all(),
        label="Template",
        required=True,
        widget=forms.Select(attrs={'class': 'form-control'}),
        empty_label="Sélectionnez une entreprise"
    )