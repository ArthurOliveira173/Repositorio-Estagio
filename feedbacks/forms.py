from django import forms
from django.forms import ModelForm
from .models import Feedbacks

class FeedbacksForm(ModelForm):

    class Meta:
        model = Feedbacks
        fields = ('fee_titulo', 'fee_descricao', 'fee_data', 'fee_arquivo', 'fee_acompanhamento')
        labels = {
            'fee_titulo': 'Escolha o tipo de Feedback',
            'fee_descricao': 'Digite com suas palavras oque aconteceu.',
            'fee_data': 'Dia da Ocasião',
            'fee_arquivo': 'Anexe um arquivo abaixo',
            'fee_acompanhamento': 'Defina o numero do acompanhamento',
        }
        widgets = {
            'fee_titulo': forms.Select(attrs={'class':'form-control', 'placeholder': 'Titulo'}),
            'fee_descricao': forms.Textarea(attrs={'class':'form-control', 'rows':5, 'placeholder': 'Descricao'}),
            'fee_data': forms.DateInput(attrs={'class':'form-control'}),
            'fee_arquivo': forms.FileInput(attrs={'class':'form-control'}),
        }

class FeedbacksRespostaForm(ModelForm):

    class Meta:
        model = Feedbacks
        fields = ('fee_titulo', 'fee_descricao', 'fee_data', 'fee_arquivo',  'fee_anterior', 'fee_proximo')
        labels = {
            'fee_titulo': 'Escolha o tipo de Feedback',
            'fee_descricao': 'Digite com suas palavras oque aconteceu.',
            'fee_data': 'Dia da Ocasião',
            'fee_arquivo': 'Anexe um arquivo abaixo',
        }
        widgets = {
            'fee_titulo': forms.Select(attrs={'class':'form-control', 'placeholder': 'Titulo'}),
            'fee_descricao': forms.Textarea(attrs={'class':'form-control', 'rows':5, 'placeholder': 'Descricao'}),
            'fee_data': forms.DateInput(attrs={'class':'form-control'}),
            'fee_arquivo': forms.FileInput(attrs={'class':'form-control'}),
        }