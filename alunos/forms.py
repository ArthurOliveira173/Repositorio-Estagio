from django import forms
from django.forms import ModelForm
from .models import AlunoPcd

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