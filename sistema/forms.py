from django import forms
from django.forms import ModelForm
from .models import Enderecos

class EnderecosForm(ModelForm):

    class Meta:
        model = Enderecos
        fields = ('end_cep', 'end_descricao', 'end_cidade')
        labels = {
            'end_cep': 'Digite o CEP',
            'end_descricao': 'Descreva o endereco',
            'end_cidade': 'Defina a cidade',
        }
        widgets = {
            'end_cep': forms.TextInput(attrs={'class':'form-control', 'placeholder': 'CEP'}),
            'end_descricao': forms.TextInput(attrs={'class':'form-control', 'placeholder': 'Descricao'}),
            'end_cidade': forms.Select(attrs={'class':'form-control', 'placeholder': 'Cidade'}),
        }