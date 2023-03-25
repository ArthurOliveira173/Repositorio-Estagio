from django import forms
from django.forms import ModelForm
from .models import Feedbacks

class FeedbacksForm(ModelForm):

    class Meta:
        model = Feedbacks
        fields = ('fee_titulo', 'fee_descricao', 'fee_arquivo', 'fee_acompanhamento')
        labels = {
            'fee_titulo': 'Escolha o tipo de Feedback',
            'fee_descricao': 'Digite a mensagem de feedback.',
            'fee_arquivo': 'Anexe um arquivo abaixo',

        }
        widgets = {
            'fee_titulo': forms.Select(attrs={'class':'form-control', 'placeholder': 'Titulo'}),
            'fee_descricao': forms.Textarea(attrs={'class':'form-control', 'rows':5, 'placeholder': 'Descricao'}),
            'fee_arquivo': forms.FileInput(attrs={'class':'form-control'}),
            'fee_acompanhamento': forms.TextInput(attrs={'type': 'hidden'}),
        }
class FeedbacksRespostaForm(ModelForm):

    class Meta:
        model = Feedbacks
        fields = ('fee_descricao', 'fee_arquivo',  'fee_anterior',  'fee_proximo')
        labels = {
            'fee_descricao': 'Digite a mensagem de feedback.',
            'fee_arquivo': 'Anexe um arquivo abaixo',
        }
        widgets = {
            'fee_descricao': forms.Textarea(attrs={'class':'form-control', 'rows':5, 'placeholder': 'Descricao'}),
            'fee_arquivo': forms.FileInput(attrs={'class':'form-control'}),
            'fee_anterior': forms.TextInput(attrs={'type': 'hidden'}),
            'fee_proximo': forms.TextInput(attrs={'type': 'hidden'}),
        }