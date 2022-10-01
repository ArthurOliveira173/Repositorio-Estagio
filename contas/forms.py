from django.contrib.auth.forms import UserCreationForm
from django.db import transaction
from django import forms
from .models import AlunoPcd, Administrador, Monitor, Tutor, Interprete, User


class AlunoForms(UserCreationForm):
    nome = forms.CharField(required=True)
    cpf = forms.CharField(required=True)
    sexo = forms.CharField(required=True)
    email = forms.CharField(required=True)
    alu_telefone = forms.CharField(required=True)
    alu_matricula = forms.CharField(required=True)
    alu_deficiencias = forms.CharField(required=True)
    alu_periodo_academico = forms.CharField(required=True)  # Field name made lowercase.
    alu_data_nascimento = forms.DateField(required=True)
    class Meta(UserCreationForm.Meta):
        model = User

    @transaction.atomic
    def data_save(self):
        usuario = super().save(commit=False)
        usuario.nome = self.cleaned_data.get('nome')
        usuario.cpf = self.cleaned_data.get('cpf')
        usuario.sexo = self.cleaned_data.get('sexo')
        usuario.email = self.cleaned_data.get('email')
        usuario.is_aluno = True
        usuario.save()
        aluno = AlunoPcd.objects.create(user=usuario)
        aluno.telefone = self.cleaned_data.get('alu_telefone')
        aluno.matricula = self.cleaned_data.get('alu_matricula')
        aluno.deficiencias = self.cleaned_data.get('alu_deficiencias')
        aluno.periodo = self.cleaned_data.get('alu_periodo_academico')
        aluno.dataNascimento = self.cleaned_data.get('alu_data_nascimento')

        aluno.save()
        return usuario

class AdministradorForms(UserCreationForm):
    nome = forms.CharField(required=True)
    cpf = forms.CharField(required=True)
    sexo = forms.CharField(required=True)
    email = forms.CharField(required=True)

    class Meta(UserCreationForm.Meta):
        model = User

    @transaction.atomic
    def data_save(self):
        usuario = super().save(commit=False)
        usuario.nome = self.cleaned_data.get('nome')
        usuario.cpf = self.cleaned_data.get('cpf')
        usuario.sexo = self.cleaned_data.get('sexo')
        usuario.email = self.cleaned_data.get('email')
        usuario.is_administrador = True
        usuario.save()
        administrador = Administrador.objects.create(user=usuario)

        administrador.save()
        return usuario

class MonitorForms(UserCreationForm):
    nome = forms.CharField(required=True)
    cpf = forms.CharField(required=True)
    sexo = forms.CharField(required=True)
    email = forms.CharField(required=True)
    mon_telefone = forms.CharField(required=True)
    mon_matricula = forms.CharField(required=True)
    mon_periodo_academico = forms.CharField(required=True)  # Field name made lowercase.
    mon_tipo = forms.CharField(required=True)
    class Meta(UserCreationForm.Meta):
        model = User

    @transaction.atomic
    def data_save(self):
        usuario = super().save(commit=False)
        usuario.nome = self.cleaned_data.get('nome')
        usuario.cpf = self.cleaned_data.get('cpf')
        usuario.sexo = self.cleaned_data.get('sexo')
        usuario.email = self.cleaned_data.get('email')
        usuario.is_monitor = True
        usuario.save()
        monitor = Monitor.objects.create(user=usuario)
        monitor.telefone = self.cleaned_data.get('mon_telefone')
        monitor.matricula = self.cleaned_data.get('mon_matricula')
        monitor.periodo = self.cleaned_data.get('mon_periodo_academico')
        monitor.tipo = self.cleaned_data.get('mon_tipo')

        monitor.save()
        return usuario

class TutorForms(UserCreationForm):
    nome = forms.CharField(required=True)
    cpf = forms.CharField(required=True)
    sexo = forms.CharField(required=True)
    email = forms.CharField(required=True)
    tut_telefone = forms.CharField(required=True)
    tut_matricula = forms.CharField(required=True)
    tut_periodo_academico = forms.CharField(required=True)  # Field name made lowercase.
    tut_tipo = forms.CharField(required=True)
    class Meta(UserCreationForm.Meta):
        model = User

    @transaction.atomic
    def data_save(self):
        usuario = super().save(commit=False)
        usuario.nome = self.cleaned_data.get('nome')
        usuario.cpf = self.cleaned_data.get('cpf')
        usuario.sexo = self.cleaned_data.get('sexo')
        usuario.email = self.cleaned_data.get('email')
        usuario.is_monitor = True
        usuario.save()
        tutor = Tutor.objects.create(user=usuario)
        tutor.telefone = self.cleaned_data.get('tut_telefone')
        tutor.matricula = self.cleaned_data.get('tut_matricula')
        tutor.periodo = self.cleaned_data.get('tut_periodo_academico')
        tutor.tipo = self.cleaned_data.get('tut_tipo')

        tutor.save()
        return usuario

class InterpreteForms(UserCreationForm):
    nome = forms.CharField(required=True)
    cpf = forms.CharField(required=True)
    sexo = forms.CharField(required=True)
    email = forms.CharField(required=True)
    int_telefone = forms.CharField(required=True)
    class Meta(UserCreationForm.Meta):
        model = User

    @transaction.atomic
    def data_save(self):
        usuario = super().save(commit=False)
        usuario.nome = self.cleaned_data.get('nome')
        usuario.cpf = self.cleaned_data.get('cpf')
        usuario.sexo = self.cleaned_data.get('sexo')
        usuario.email = self.cleaned_data.get('email')
        usuario.is_interprete = True
        usuario.save()
        interprete = Interprete.objects.create(user=usuario)
        interprete.telefone = self.cleaned_data.get('int_telefone')

        interprete.save()
        return usuario