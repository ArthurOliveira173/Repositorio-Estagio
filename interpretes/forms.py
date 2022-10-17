from django import forms
from django.forms import ModelForm
from .models import Interprete

class InterpretesForm(ModelForm):

    class Meta:
        model = Interprete
        fields = ('int_nome', 'int_cpf', 'int_genero', 'int_email_pessoal', 'int_email_institucional', 'int_telefone')
        labels = {
            'int_nome': 'Digite o nome',
            'int_cpf': 'Digite o CPF',
            'int_genero': 'Defina o genero',
            'int_email_pessoal': 'Digite o email pessoal',
            'int_email_institucional': 'Digite o email institucional',
            'int_telefone': 'Digite o contato',
        }
        widgets = {
            'int_nome': forms.TextInput(attrs={'class':'form-control', 'placeholder': 'Nome'}),
            'int_cpf': forms.TextInput(attrs={'class':'form-control', 'placeholder': 'CPF'}),
            'int_email_pessoal': forms.EmailInput(attrs={'class':'form-control', 'placeholder': 'Email pessoal'}),
            'int_email_institucional': forms.EmailInput(attrs={'class':'form-control', 'placeholder': 'Email Institucional'}),
            'int_telefone': forms.TextInput(attrs={'class':'form-control', 'placeholder': 'Telefone'}),
        }