from django import forms
from django.forms import ModelForm
from .models import Avisos
from portal import settings

class AvisosForm(ModelForm):

    class Meta:
        model = Avisos
        fields = ['avi_titulo', 'avi_descricao', 'avi_data', 'avi_arquivos', 'avi_mostrar']

        labels = {
            'avi_titulo': 'Digite o nome do aviso',
            'avi_descricao': 'Digite a descricao do aviso',
            'avi_data': 'Defina a Data do aviso',
            'avi_arquivos': 'Anexe um arquivo abaixo',
            'avi_mostrar': 'Defina o estado de visualizacao',
        }
        widgets = {
            'avi_titulo': forms.TextInput(attrs={'class':'form-control', 'placeholder': 'Titulo'}),
            'avi_descricao': forms.Textarea(attrs={'type': 'text', 'class': 'form-control', 'placeholder': 'Descrição', 'rows': '10'}),
            'avi_data': forms.DateTimeInput(format="%Y-%m-%d %H:%M", attrs={'class':'form-control', 'placeholder': 'dia/mês/ano Hora:Minutos'}),
            'avi_arquivos': forms.FileInput(attrs={'class':'form-control'}),
            'avi_mostrar': forms.CheckboxInput(attrs={'class':'form-control'}),
        }
