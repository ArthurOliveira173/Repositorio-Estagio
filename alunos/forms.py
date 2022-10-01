# from django.contrib.auth.forms import UserCreationForm
# from django.db import transaction
# from django import forms
# from .models import AlunoPcd, User
#
#
# class AlunoForms(UserCreationForm):
#     nome = forms.CharField(required=True)
#     cpf = forms.CharField(required=True)
#     sexo = forms.CharField(required=True)
#     email = forms.CharField(required=True)
#     alu_telefone = forms.CharField(required=True)
#     alu_matricula = forms.CharField(required=True)
#     alu_deficiencias = forms.CharField(required=True)
#     alu_cur = forms.CharField(required=True)
#     alu_dis = forms.CharField(required=True)
#     alu_periodo_academico = forms.CharField(required=True)  # Field name made lowercase.
#     alu_data_nascimento = forms.DateField(required=True)
#     class Meta(UserCreationForm.Meta):
#         model = User
#
#     @transaction.atomic
#     def data_save(self):
#         usuario = super().save(commit=False)
#         usuario.nome = self.cleaned_data.get('nome')
#         usuario.cpf = self.cleaned_data.get('cpf')
#         usuario.sexo = self.cleaned_data.get('sexo')
#         usuario.email = self.cleaned_data.get('email')
#         usuario.is_aluno = True
#         usuario.save()
#         aluno = AlunoPcd.objects.create(user=usuario)
#         aluno.nome = self.cleaned_data.get('alu_telefone')
#         aluno.nome = self.cleaned_data.get('alu_matricula')
#         aluno.nome = self.cleaned_data.get('alu_deficiencias')
#
#         aluno.nome = self.cleaned_data.get('alu_cur')
#
#         aluno.nome = self.cleaned_data.get('alu_dis')
#         aluno.nome = self.cleaned_data.get('alu_periodo_academico')
#         aluno.nome = self.cleaned_data.get('alu_data_nascimento')
#
#         aluno.save()
#         return usuario