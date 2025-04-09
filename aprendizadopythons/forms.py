from django import forms
from .models import Topico
from .models import Entrada


class Topico_form(forms.ModelForm):
    class Meta:
        model = Topico
        fields = ['text']
        labels = {'text': ''}

class Entrada_form(forms.ModelForm):
    class Meta:
        model = Entrada
        fields = ['text']
        labels = {'text': ''}
        widgets = {'text': forms.Textarea(attrs={'cols':80})}