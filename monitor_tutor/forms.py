from django import forms
from django.forms import ModelForm
from .models import Monitor, Tutor

class MonitoresForm(ModelForm):

    class Meta:
        model = Monitor
        fields = ('mon_nome', 'mon_cpf', 'mon_genero', 'mon_email_pessoal', 'mon_email_institucional', 'mon_telefone',
                  'mon_endereco', 'mon_matricula', 'mon_curso', 'mon_periodo_academico')
        labels = {
            'mon_nome': 'Digite o nome',
            'mon_cpf': 'Digite o CPF',
            'mon_genero': 'Defina o genero',
            'mon_email_pessoal': 'Digite o email pessoal',
            'mon_email_institucional': 'Digite o email institucional',
            'mon_telefone': 'Digite o contato',
            'mon_endereco': 'Defina o endereco',
            'mon_matricula': 'Digite a matricula',
            'mon_curso': 'Defina o curso',
            'mon_periodo_academico': 'Defina o periodo academico',
        }
        widgets = {
            'mon_nome': forms.TextInput(attrs={'class':'form-control', 'placeholder': 'Nome'}),
            'mon_cpf': forms.TextInput(attrs={'class':'form-control', 'placeholder': 'CPF'}),
            'mon_email_pessoal': forms.EmailInput(attrs={'class':'form-control', 'placeholder': 'Email pessoal'}),
            'mon_email_institucional': forms.EmailInput(attrs={'class':'form-control', 'placeholder': 'Email Institucional'}),
            'mon_telefone': forms.TextInput(attrs={'class':'form-control', 'placeholder': 'Telefone'}),
            'mon_matricula': forms.TextInput(attrs={'class':'form-control', 'placeholder': 'Matricula'}),
            'mon_curso': forms.Select(attrs={'class':'form-control', 'placeholder': 'Curso'}),
            'mon_endereco': forms.Select(attrs={'class': 'form-control', 'placeholder': 'Endereco'}),
            'mon_periodo_academico': forms.TextInput(attrs={'class':'form-control', 'placeholder': 'Periodo'}),
        }

class TutoresForm(ModelForm):

    class Meta:
        model = Tutor
        fields = ('tut_nome', 'tut_cpf', 'tut_genero', 'tut_email_pessoal', 'tut_email_institucional', 'tut_telefone',
                  'tut_endereco', 'tut_matricula', 'tut_curso', 'tut_periodo_academico')
        labels = {
            'tut_nome': 'Digite o nome',
            'tut_cpf': 'Digite o CPF',
            'tut_genero': 'Defina o genero',
            'tut_email_pessoal': 'Digite o email pessoal',
            'tut_email_institucional': 'Digite o email institucional',
            'tut_telefone': 'Digite o contato',
            'tut_endereco': 'Defina o endereco',
            'tut_matricula': 'Digite a matricula',
            'tut_curso': 'Defina o curso',
            'tut_periodo_academico': 'Defina o periodo academico',
        }
        widgets = {
            'tut_nome': forms.TextInput(attrs={'class':'form-control', 'placeholder': 'Nome'}),
            'tut_cpf': forms.TextInput(attrs={'class':'form-control', 'placeholder': 'CPF'}),
            'tut_email_pessoal': forms.EmailInput(attrs={'class':'form-control', 'placeholder': 'Email pessoal'}),
            'tut_email_institucional': forms.EmailInput(attrs={'class':'form-control', 'placeholder': 'Email Institucional'}),
            'tut_telefone': forms.TextInput(attrs={'class':'form-control', 'placeholder': 'Telefone'}),
            'tut_matricula': forms.TextInput(attrs={'class':'form-control', 'placeholder': 'Matricula'}),
            'tut_curso': forms.Select(attrs={'class':'form-control', 'placeholder': 'Curso'}),
            'tut_endereco': forms.Select(attrs={'class': 'form-control', 'placeholder': 'Endereco'}),
            'tut_periodo_academico': forms.TextInput(attrs={'class':'form-control', 'placeholder': 'Periodo'}),
        }