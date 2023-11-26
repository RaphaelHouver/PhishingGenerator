from django import forms
from .models import entreprise

class EntrepriseForm(forms.Form):
    entreprise = forms.ModelChoiceField(queryset=entreprise.objects.all(), empty_label=None, label='Nom de l\'entreprise')