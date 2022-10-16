from django import forms
from django.forms import ModelForm
from .models import Acompanhamentos

class AcompanhamentosForm(ModelForm):

    class Meta:
        model = Acompanhamentos
        fields = ('aco_semestre', 'aco_inicio', 'aco_fim', 'aco_aluno_pcd')
        labels = {
            'aco_semestre': 'Digite o semestre do acompanhamento',
            'aco_inicio': 'Defina a data inicial do acompanhamento',
            'aco_fim': 'Defina a data final do acompanhamento',
            'aco_aluno_pcd': 'Defina o aluno acompanhado',
        }
        widgets = {
            'aco_semestre': forms.TextInput(attrs={'class':'form-control', 'placeholder': '____._'}),
            'aco_inicio': forms.DateInput(attrs={'class':'form-control'}),
            'aco_fim': forms.DateInput(attrs={'class':'form-control'}),
        }
