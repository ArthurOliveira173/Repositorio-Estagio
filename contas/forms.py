from django.contrib.auth.forms import UserCreationForm
from django.db import transaction
from django import forms
from django.apps import apps
modelAluno = apps.get_model("alunos", "AlunoPcd")
modelAdministrador = apps.get_model("administrador", "Administrador")
modelMonitor = apps.get_model("monitor_tutor", "Monitor")
modelTutor = apps.get_model("monitor_tutor", "Tutor")
modelInterprete = apps.get_model("interpretes", "Interprete")
from .models import User


class AlunoForms(UserCreationForm):
    nome = forms.CharField(required=True)
    cpf = forms.CharField(required=True)
    sexo = forms.CharField(required=True)
    email = forms.EmailField(required=True)
    telefone = forms.CharField(required=True)
    matricula = forms.CharField(required=True)
    deficiencias = forms.CharField(required=True)
    periodo_academico = forms.CharField(required=True)  # Field name made lowercase.
    data_nascimento = forms.DateField(required=True)
    class Meta(UserCreationForm.Meta):
        model = User

    @transaction.atomic
    def data_save(self):
        usuario = super().save(commit=False)
        usuario.is_aluno = True
        usuario.save()
        aluno = modelAluno.objects.create(user=usuario)
        aluno.nome = self.cleaned_data.get('nome')
        aluno.cpf = self.cleaned_data.get('cpf')
        aluno.sexo = self.cleaned_data.get('sexo')
        aluno.email = self.cleaned_data.get('email')
        aluno.telefone = self.cleaned_data.get('telefone')
        aluno.matricula = self.cleaned_data.get('matricula')
        aluno.deficiencias = self.cleaned_data.get('deficiencias')
        aluno.periodo = self.cleaned_data.get('periodo_academico')
        aluno.dataNascimento = self.cleaned_data.get('data_nascimento')

        aluno.save()
        return usuario

class AdministradorForms(UserCreationForm):
    nome = forms.CharField(required=True)
    cpf = forms.CharField(required=True)
    sexo = forms.CharField(required=True)
    email = forms.EmailField(required=True)

    class Meta(UserCreationForm.Meta):
        model = User

    @transaction.atomic
    def data_save(self):
        usuario = super().save(commit=False)
        usuario.is_administrador = True
        usuario.save()
        administrador = modelAdministrador.objects.create(user=usuario)
        administrador.nome = self.cleaned_data.get('nome')
        administrador.cpf = self.cleaned_data.get('cpf')
        administrador.sexo = self.cleaned_data.get('sexo')
        administrador.email = self.cleaned_data.get('email')

        administrador.save()
        return usuario

class MonitorForms(UserCreationForm):
    nome = forms.CharField(required=True)
    cpf = forms.CharField(required=True)
    sexo = forms.CharField(required=True)
    email = forms.EmailField(required=True)
    telefone = forms.CharField(required=True)
    matricula = forms.CharField(required=True)
    periodo_academico = forms.CharField(required=True)  # Field name made lowercase.
    tipo = forms.CharField(required=True)
    class Meta(UserCreationForm.Meta):
        model = User

    @transaction.atomic
    def data_save(self):
        usuario = super().save(commit=False)
        usuario.is_monitor = True
        usuario.save()
        monitor = modelMonitor.objects.create(user=usuario)
        monitor.nome = self.cleaned_data.get('nome')
        monitor.cpf = self.cleaned_data.get('cpf')
        monitor.sexo = self.cleaned_data.get('sexo')
        monitor.email = self.cleaned_data.get('email')
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
    email = forms.EmailField(required=True)
    telefone = forms.CharField(required=True)
    matricula = forms.CharField(required=True)
    periodo_academico = forms.CharField(required=True)  # Field name made lowercase.
    tipo = forms.CharField(required=True)
    class Meta(UserCreationForm.Meta):
        model = User

    @transaction.atomic
    def data_save(self):
        usuario = super().save(commit=False)
        usuario.is_monitor = True
        usuario.save()
        tutor = modelTutor.objects.create(user=usuario)
        tutor.nome = self.cleaned_data.get('nome')
        tutor.cpf = self.cleaned_data.get('cpf')
        tutor.sexo = self.cleaned_data.get('sexo')
        tutor.email = self.cleaned_data.get('email')
        tutor.telefone = self.cleaned_data.get('telefone')
        tutor.matricula = self.cleaned_data.get('matricula')
        tutor.periodo = self.cleaned_data.get('periodo_academico')
        tutor.tipo = self.cleaned_data.get('tipo')

        tutor.save()
        return usuario

class InterpreteForms(UserCreationForm):
    nome = forms.CharField(required=True)
    cpf = forms.CharField(required=True)
    sexo = forms.CharField(required=True)
    email = forms.EmailField(required=True)
    int_telefone = forms.CharField(required=True)
    class Meta(UserCreationForm.Meta):
        model = User

    @transaction.atomic
    def data_save(self):
        usuario = super().save(commit=False)
        usuario.is_interprete = True
        usuario.save()
        interprete = modelInterprete.objects.create(user=usuario)
        interprete.nome = self.cleaned_data.get('int_nome')
        interprete.cpf = self.cleaned_data.get('int_cpf')
        interprete.sexo = self.cleaned_data.get('int_sexo')
        interprete.email = self.cleaned_data.get('int_email')
        interprete.telefone = self.cleaned_data.get('int_telefone')

        interprete.save()
        return usuario