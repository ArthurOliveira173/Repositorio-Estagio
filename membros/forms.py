from django import forms
from django.forms import ModelForm
from .models import AlunoPcd, Monitor, Tutor, Interprete

class AlunosForm(ModelForm):
    alu_endereco = forms.CheckboxInput()

    class Meta:
        model = AlunoPcd
        fields = ('alu_nome', 'alu_cpf', 'alu_genero', 'alu_email_pessoal', 'alu_email_institucional', 'alu_telefone',
                  'alu_endereco', 'alu_matricula', 'alu_deficiencias', 'alu_curso', 'alu_periodo_academico', 'alu_data_nascimento')
        labels = {
            'alu_nome': 'Digite o nome',
            'alu_cpf': 'Digite o CPF',
            'alu_genero': 'Defina o genero',
            'alu_email_pessoal': 'Digite o email pessoal',
            'alu_email_institucional': 'Digite o email institucional',
            'alu_telefone': 'Digite o contato',
            'alu_endereco': 'Defina o endereco',
            'alu_matricula': 'Digite a matricula',
            'alu_deficiencias': 'Cite as deficiencias',
            'alu_curso': 'Defina o curso',
            'alu_periodo_academico': 'Defina o periodo academico',
            'alu_data_nascimento': 'Defina a data de nascimento',
        }
        widgets = {
            'alu_nome': forms.TextInput(attrs={'class':'form-control', 'placeholder': 'Nome'}),
            'alu_cpf': forms.TextInput(attrs={'class':'form-control', 'placeholder': 'CPF'}),
            'alu_email_pessoal': forms.EmailInput(attrs={'class':'form-control', 'placeholder': 'Email pessoal'}),
            'alu_email_institucional': forms.EmailInput(attrs={'class':'form-control', 'placeholder': 'Email Institucional'}),
            'alu_telefone': forms.TextInput(attrs={'class':'form-control', 'placeholder': 'Telefone'}),
            'alu_matricula': forms.TextInput(attrs={'class':'form-control', 'placeholder': 'Matricula'}),
            'alu_deficiencias': forms.TextInput(attrs={'class':'form-control', 'placeholder': 'Deficiencias'}),
            'alu_curso': forms.Select(attrs={'class':'form-control', 'placeholder': 'Curso'}),
            'alu_endereco': forms.Select(attrs={'class': 'form-control', 'placeholder': 'Endereco'}),
            'alu_periodo_academico': forms.TextInput(attrs={'class':'form-control', 'placeholder': 'Periodo'}),
            'alu_data_nascimento': forms.DateInput(attrs={'class':'date', 'placeholder': '____-__-__'})
        }

    def __init__(self, *args, **kwargs):
        super(AlunosForm, self).__init__(*args, **kwargs)
        self.fields['alu_endereco'].widget.attrs['data-toggle'] = "modal"
        self.fields['alu_endereco'].widget.attrs['data-target'] = "#exampleModal"

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