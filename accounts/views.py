from django.contrib import messages, auth
from django.contrib.auth import authenticate
from django.core.validators import validate_email
from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.models import User, Group
from django.contrib.auth.decorators import login_required
from django.contrib.auth import authenticate, login, logout
from django.views import View
from . import forms
from membros.models import AlunoPcd
from django.http import HttpResponse
# Create your views here.


class Login(View):
     def post(self, *args, **kwargs):
        username = self.request.POST.get('usuario')
        password = self.request.POST.get('senha')

        if not username or not password:
            messages.error(
                self.request,
                'Usuário ou senha inválidos.'
            )
            return redirect('accounts:login')

        usuario = authenticate(
            self.request, username=username, password=password)

        if not usuario:
            messages.error(
                self.request,
                'Usuário ou senha inválidos.'
            )
            return redirect('accounts:login')

        login(self.request, user=usuario)

        messages.success(
            self.request,
            'Você fez login.'
        )
        return redirect('accounts:cadastroAluno')

class Logout(View):
    def get(self, *args, **kwargs):
        logout(self.request)
        return redirect('login')


class Atualizar(View):
    def get(self, *args, **kwargs):
        return HttpResponse('Atualizar')

class BaseCadastro(View):
    template_name = 'accounts/cadastroAluno.html'
    def setup(self, *args, **kwargs):
        super().setup(*args, **kwargs)

        self.aluno = None

        #Se o usuário estiver logado
        if self.request.user.is_authenticated:
            self.aluno = AlunoPcd.objects.filter(alu_user=self.request.user).first()

            self.contexto = {
                'userform': forms.UserForm(
                    data = self.request.POST or None,
                    usuario= self.request.user,
                    instance= self.request.user,
                ),
                'alunoform': forms.AlunoForm(
                    data = self.request.POST or None,
                    instance = self.aluno,

                )
            }
        # Se o usuário não estiver logado
        else:
            self.contexto = {
                'userform': forms.UserForm(
                    data=self.request.POST or None
                ),
                'alunoform': forms.AlunoForm(
                    data=self.request.POST or None
                )
            }
        self.userform = self.contexto['userform']
        self.alunoform = self.contexto['alunoform']

        self.renderizar = render(self.request, self.template_name, self.contexto)

        if self.request.user.is_authenticated:
            self.template_name = 'accounts/atualizar.html'

    def get(self, *args, **kwargs):
        return self.renderizar


class CadastroAluno(BaseCadastro):
    def post(self, *args, **kwargs):
        print(self.aluno)
        if not self.userform.is_valid():
            messages.error(
                self.request,
                'Existem erros no formulário de cadastro. Verifique se todos '
                'os campos foram preenchidos corretamente.'
            )
            return self.renderizar

        first_name = self.userform.cleaned_data.get('first_name')
        last_name = self.userform.cleaned_data.get('last_name')
        username = self.userform.cleaned_data.get('username')
        password = self.userform.cleaned_data.get('password')
        email = self.userform.cleaned_data.get('email')

        #usuário está logado
        if self.request.user.is_authenticated:
            usuario = get_object_or_404(User, username=self.request.user.username)
            usuario.username = username

            if password:
                usuario.set_password(password)

            usuario.email = email
            usuario.first_name = first_name
            usuario.last_name = last_name
            usuario.save()

        #usuário não logado (novo usuário)
        else:
            usuario = self.userform.save(commit=False)
            usuario.set_password(password)
            usuario.save()

            alunoPcd = self.alunoform.save(commit=False)
            alunoPcd.alu_nome = first_name+' '+last_name
            alunoPcd.alu_cpf = username
            alunoPcd.alu_email_pessoal = email
            alunoPcd.alu_user = usuario
            alunoPcd.save()

        if password:
            autentica = authenticate(self.request, username=usuario, password=password)
            if autentica:
                print(autentica)
                login(self.request, user=usuario)

        return self.renderizar




