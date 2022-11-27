import string

from django.contrib import messages, auth
from django.contrib.auth import authenticate
from django.core.validators import validate_email
from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.models import User, Group
from django.contrib.auth.decorators import login_required
from string import ascii_letters

import membros.models
from .models import FormAdministrador, FormMonitor, FormTutor
from membros.forms import AlunosForm, MonitoresForm, TutoresForm
from django.views import View
from . import forms
from . import models
from membros.models import AlunoPcd
# Create your views here.


def login(request):
    if request.method != 'POST':
        return render(request, 'accounts/login.html')
    usuario = request.POST.get('usuario')
    senha = request.POST.get('senha')

    user = auth.authenticate(request, username=usuario, password=senha)

    if not user:
        messages.error(request, 'usuario ou senha invalidos.')
        return render(request, 'accounts/login.html')
    else:
        auth.login(request, user)
        messages.success(request, 'Login com sucesso.')
        return redirect('aviIndexAluno')

def logout(request):
    auth.logout(request)
    return redirect('dashboard')

def cadastro(request):
    if request.method != 'POST':
        return render(request, 'accounts/cadastro.html')

    nome = request.POST.get('nome')
    sobrenome = request.POST.get('sobrenome')
    usuario = request.POST.get('cpf')
    email = request.POST.get('email')
    senha = request.POST.get('senha')
    senha2 = request.POST.get('senha2')

    if not nome or not sobrenome or not usuario or not email or not senha or not senha2:
        messages.error(request, 'Todos os campos devem ser preenchidos')
        return render(request, 'accounts/cadastro.html')

    try:
        validate_email(email)
    except:
        messages.error(request, 'Email invalido.')
        return render(request, 'accounts/cadastro.html')



    if len(usuario) > 14:
        messages.error(request, 'Cpf deve ter 14 caracteres.')
        return render(request, 'accounts/cadastro.html')

    if User.objects.filter(username=usuario).exists():
        messages.error(request, 'Cpf ja cadastrado, verifique e tente novamente!')
        return render(request, 'accounts/cadastro.html')


    if User.objects.filter(email=email).exists():
        messages.error(request, 'Email ja cadastrado')
        return render(request, 'accounts/cadastro.html')

    if len(senha) < 6:
        messages.error(request, 'Senha precisa ter 6 caracteres ou mais.')
        return render(request, 'accounts/cadastro.html')

    if senha != senha2:
        messages.error(request, 'Confirme as SENHAS novamente!')
        return render(request, 'accounts/cadastro.html')

    messages.success(request, 'Registrado com sucesso! Agora faca login.')

    user = User.objects.create_user(username=usuario, email=email,
                                    password=senha, first_name=nome,
                                    last_name=sobrenome)
    user.save()
    return redirect('login')

@login_required(redirect_field_name='login')
def dashboard(request):
    if request.method != 'POST':
        form = FormAdministrador()
        return render(request, 'accounts/dashboard.html', {'form': form})

    form = FormAdministrador(request.POST, request.FILES)

    if not form.is_valid():
        messages.error(request, 'Erro ao enviar suas informacoes')
        form = FormAdministrador(request.POST)
        return render(request, 'accounts/dashboard.html', {'form': form})

    nome = request.POST.get('adm_nome')
    if len(nome) < 5:
        messages.error(request, '"Nome" deve ter que 5 caracteres')
        form = FormAdministrador(request.POST)
        return render(request, 'accounts/dashboard.html', {'form': form})

    form.save()
    messages.success(request, f'Usuario {request.POST.get("adm_nome")} salvo com sucesso!')
    return redirect('dashboard')



class BaseCadastro(View):
    template_name = 'accounts/cadastroAluno.html'
    def setup(self, *args, **kwargs):
        super().setup(*args, **kwargs)

        self.alunoPcd = None

        #Se o usuário estiver logado
        if self.request.user.is_authenticated:
            self.alunoPcd = AlunoPcd.objects.filter(alu_user=self.request.user).first()

            self.contexto = {
                'userform': forms.UserForm(
                    data = self.request.POST or None,
                    usuario= self.request.user,
                    instance= self.request.user,
                ),
                'alunoform': forms.AlunoForm(
                    data = self.request.POST or None,
                    instance = self.alunoPcd
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
    def get(self, *args, **kwargs):
        return self.renderizar


class CadastroAluno(BaseCadastro):
    def post(self, *args, **kwargs):
        if not self.userform.is_valid() or not self.alunoform.is_valid():
            return self.renderizar

        first_name = self.userform.cleaned_data.get('first_name')
        last_name = self.userform.cleaned_data.get('last_name')
        username= self.userform.cleaned_data.get('username')
        password= self.userform.cleaned_data.get('password')
        email= self.userform.cleaned_data.get('email')

        if self.request.user.is_authenticated:
            pass

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

        return self.renderizar

def cadastroMonitor(request):
    if request.method != 'POST':
        form = MonitoresForm()
        return render(request, 'accounts/cadastroMonitor.html', {'form': form})

    form = MonitoresForm(request.POST, request.FILES)

    if not form.is_valid():
        messages.error(request, 'Erro ao enviar suas informacoes, tente novamente!')
        form = MonitoresForm(request.POST)
        return render(request, 'accounts/cadastroMonitor.html', {'form': form})


    nome = request.POST.get('mon_nome')
    usuario = request.POST.get('mon_cpf')
    sexo = request.POST.get('mon_genero')
    email_pessoal = request.POST.get('mon_email_pessoal')
    email_instituicao = request.POST.get('mon_email_institucional')
    telefone = request.POST.get('mon_telefone')
    cep = request.POST.get('mon_endereco_cep')
    descricao_des = request.POST.get('mon_endereco_descricao')
    cidade = request.POST.get('mon_endereco_cidade')
    curso = request.POST.get(' mon_curso')
    periodo = request.POST.get('mon_periodo_academico')
    matricula = request.POST.get('mon_matricula')
    senha = request.POST.get('senha')
    senha2 = request.POST.get('senha2')

    if not nome or not usuario or not sexo or not email_pessoal or not email_instituicao or not telefone or not cep or not descricao_des or not cidade or not periodo or not matricula or not senha or not senha2:
        messages.error(request, 'Todos os campos devem ser preenchidos!')
        return render(request, 'accounts/cadastroMonitor.html', {'form': form})

    try:
        validate_email(email_pessoal)
    except:
        messages.error(request, 'Email pessoal invalido!')
        return render(request, 'accounts/cadastroMonitor.html', {'form': form})

    try:
        validate_email(email_instituicao)
    except:
        messages.error(request, 'Email institucional invalido!')
        return render(request, 'accounts/cadastroMonitor.html', {'form': form})

    if len(usuario) > 14:
        messages.error(request, '')
        return render(request, 'accounts/cadastroMonitor.html', {'form': form})

    if User.objects.filter(username=usuario).exists():
        messages.error(request, 'Cpf ja cadastrado, verifique e tente novamente!')
        return render(request, 'accounts/cadastroMonitor.html', {'form': form})

    if User.objects.filter(email=email_pessoal).exists():
        messages.error(request, 'Email pessoal ja cadastrado!')
        return render(request, 'accounts/cadastroMonitor.html', {'form': form})

    if User.objects.filter(email=email_instituicao).exists():
        messages.error(request, 'Email institucional ja cadastrado!')
        return render(request, 'accounts/cadastroMonitor.html', {'form': form})

    if len(senha) < 6:
        messages.error(request, 'Senha precisa ter 6 caracteres ou mais!')
        return render(request, 'accounts/cadastroAluno.html',  {'form': form})

    if senha != senha2:
        messages.error(request, 'Senhas diferentes, tente novamente!')
        return render(request, 'accounts/cadastroMonitor.html')

    messages.success(request, 'Cadastro com sucesso, realize seu primeiro Login!')

    user = User.objects.create_user(username=usuario, email=email_pessoal,
                                    password=senha, first_name=nome,
                                    last_name=email_instituicao)
    form.save()
    user.save()
    return redirect('login')

def cadastroTutor(request):
    if request.method != 'POST':
        form = TutoresForm()
        return render(request, 'accounts/cadastroTutor.html', {'form': form})

    form = TutoresForm(request.POST, request.FILES)

    if not form.is_valid():
        messages.error(request, 'Erro ao enviar suas informacoes, tente novamente!')
        form = TutoresForm(request.POST)
        return render(request, 'accounts/cadastroTutor.html', {'form': form})


    nome = request.POST.get('tut_nome')
    usuario = request.POST.get('tut_cpf')
    sexo = request.POST.get('tut_genero')
    email_pessoal = request.POST.get('tut_email_pessoal')
    email_instituicao = request.POST.get('tut_email_institucional')
    telefone = request.POST.get('tut_telefone')
    cep = request.POST.get('tut_endereco_cep')
    descricao_des = request.POST.get('tut_endereco_descricao')
    cidade = request.POST.get('tut_endereco_cidade')
    curso = request.POST.get(' tut_curso')
    periodo = request.POST.get('tut_periodo_academico')
    matricula = request.POST.get('tut_matricula')
    senha = request.POST.get('senha')
    senha2 = request.POST.get('senha2')

    if not nome or not usuario or not sexo or not email_pessoal or not email_instituicao or not telefone or not cep or not descricao_des or not cidade or not periodo or not matricula or not senha or not senha2:
        messages.error(request, 'Todos os campos devem ser preenchidos!')
        return render(request, 'accounts/cadastroTutor.html', {'form': form})

    try:
        validate_email(email_pessoal)
    except:
        messages.error(request, 'Email pessoal invalido!')
        return render(request, 'accounts/cadastroTutor.html', {'form': form})

    try:
        validate_email(email_instituicao)
    except:
        messages.error(request, 'Email institucional invalido!')
        return render(request, 'accounts/cadastroTutor.html', {'form': form})

    try:
         valida_cpf(usuario)
    except:
        messages.error(request, 'Cpf nao é valido!')
        return render(request, 'accounts/cadastroTutor.html', {'form': form})

    if User.objects.filter(username=usuario).exists():
        messages.error(request, 'Cpf ja cadastrado, verifique e tente novamente!')
        return render(request, 'accounts/cadastroTutor.html', {'form': form})

    if User.objects.filter(email=email_pessoal).exists():
        messages.error(request, 'Email pessoal ja cadastrado!')
        return render(request, 'accounts/cadastroTutor.html', {'form': form})

    if User.objects.filter(email=email_instituicao).exists():
        messages.error(request, 'Email institucional ja cadastrado!')
        return render(request, 'accounts/cadastroTutor.html', {'form': form})

    if len(senha) < 6:
        messages.error(request, 'Senha precisa ter 6 caracteres ou mais.')
        return render(request, 'accounts/cadastroTutor.html', {'form': form})

    if senha != senha2:
        messages.error(request, 'Senhas diferentes, tente novamente!')
        return render(request, 'accounts/cadastroTutor.html')


    messages.success(request, 'Cadastro com sucesso, realize seu primeiro Login!')

    user = User.objects.create_user(username=usuario, email=email_pessoal,
                                    password=senha, first_name=nome,
                                    last_name=email_instituicao)
    form.save()
    user.save()
    return redirect('login')


@login_required(redirect_field_name='login')
def cadastroInterprete(request):
    if request.method != 'POST':
        form = FormAdministrador()
        return render(request, 'accounts/cadastroInterprete.html', {'form': form})

    form = FormAdministrador(request.POST, request.FILES)

    if not form.is_valid():
        messages.error(request, 'Erro ao enviar suas informacoes, tente novamente!')
        form = FormAdministrador(request.POST)
        return render(request, 'accounts/cadastroInterprete.html', {'form': form})

    nome = request.POST.get('adm_nome')
    if len(nome) < 5:
        messages.error(request, '"Nome" deve ter que 5 caracteres')
        form = FormAdministrador(request.POST)
        return render(request, 'accounts/dashboard.html', {'form': form})

    form.save()
    messages.success(request, f'Usuario {request.POST.get("adm_nome")} salvo com sucesso!')
    return redirect('dashboard')

@login_required(redirect_field_name='login')
def dashboardAluno(request):
    if request.method != 'POST':
        form = FormAlunoPcd()
        return render(request, 'accounts/dashboardAluno.html', {'form': form})

    form = FormAlunoPcd(request.POST, request.FILES)

    if not form.is_valid():
        messages.error(request, 'Erro ao enviar suas informacoes')
        form = FormAlunoPcd(request.POST)
        return render(request, 'accounts/dashboardAluno.html', {'form': form})


    form.save()
    messages.success(request, f'Usuario {request.POST.get("adm_nome")} salvo com sucesso!')
    return redirect('dashboard')




