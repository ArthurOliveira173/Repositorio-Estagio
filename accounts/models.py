from django.db import models
from membros.models import Administrador, AlunoPcd, Monitor, Tutor, Interprete
from django import forms

class FormAdministrador(forms.ModelForm):
    class Meta:
        model = Administrador
        exclude = ()

# Create your models here.

class FormAlunoPcd(forms.ModelForm):
    class Meta:
        model = AlunoPcd
        exclude = ('alu_id',)

    labels = {
        'alu_nome': 'Digite o nome completo',
    }
    widgets = {
        'alu_nome': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Nome Completo'}),
    }


class FormMonitor(forms.ModelForm):
    class Meta:
        model = Monitor
        exclude = ('mon_id',)

class FormTutor(forms.ModelForm):
    class Meta:
        model = Tutor
        exclude = ('tut_id',)


class FormInterprete(forms.ModelForm):
    class Meta:
        model = Interprete
        exclude = ('int_id',)