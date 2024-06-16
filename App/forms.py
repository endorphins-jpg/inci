from django import forms
from .models import *

class PlataformaForm(forms.ModelForm):
    class Meta:
        model = Plataforma
        fields = '__all__'

class FerramentaForm(forms.ModelForm):
    class Meta:
        model = Ferramenta
        fields = '__all__'