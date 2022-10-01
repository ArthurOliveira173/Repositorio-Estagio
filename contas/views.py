from email import message
from django.shortcuts import render, redirect
from django.contrib.auth import login, logout,authenticate
from django.contrib.auth.forms import AuthenticationForm
from django.contrib import messages
from django.views.generic import CreateView
from .models import User
from .forms import AlunoForms, AdministradorForms, MonitorForms, TutorForms, InterpreteForms

# Create your views here.

def index(request):
    return render(request, 'index.html')

def registro(request):
    return render(request, 'registro.html')

class RegistroAluno(CreateView):
    model = User
    form_class = AlunoForms
    template_name= 'registroAluno.html'

    def form_valid(self, form):
        user = form.save()
        login(self.request, user)
        return redirect('/contas/index')

class RegistroAdministrador(CreateView):
    model = User
    form_class = AdministradorForms
    template_name= 'registroAdministrador.html'

    def form_valid(self, form):
        user = form.save()
        login(self.request, user)
        return redirect('/contas/index')

class RegistroMonitor(CreateView):
    model = User
    form_class = MonitorForms
    template_name= 'registroMonitor.html'

    def form_valid(self, form):
        user = form.save()
        login(self.request, user)
        return redirect('/contas/index')

class RegistroTutor(CreateView):
    model = User
    form_class = TutorForms
    template_name= 'registroTutor.html'

    def form_valid(self, form):
        user = form.save()
        login(self.request, user)
        return redirect('/contas/index')

class RegistroInterprete(CreateView):
    model = User
    form_class = InterpreteForms
    template_name= 'registroInterprete.html'

    def form_valid(self, form):
        user = form.save()
        login(self.request, user)
        return redirect('/contas/index')

def loginUsuario(request):
    if request.method=='POST':
        form = AuthenticationForm(data=request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            user = authenticate(username=username, password=password)
            if user is not None :
                login(request,user)
                return redirect('/contas/index')
            else:
                messages.error(request,"Dados de usuário ou senha inválidos")
        else:
            messages.error(request,"Dados de usuário ou senha inválidos")
    return render(request, 'login.html',context={'form':AuthenticationForm()})

def logoutUsuario(request):
    logout(request)
    return redirect('/contas/index')
