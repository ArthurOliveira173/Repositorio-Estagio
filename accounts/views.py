from django.contrib import messages
from django.shortcuts import render

# Create your views here.

def login(request):
    return render(request, 'accounts/login.html')

def logout(request):
    return render(request, 'accounts/logout.html')

def cadastro(request):
    if request.method != 'POST':
        return render(request, 'accounts/cadastro.html')

    nome = request.POST.get('nome')
    cpf = request.POST.get('cpf')
    sexo = request.POST.get('sexo')
    email = request.POST.get('email')
    senha = request.POST.get('senha')
    senha2 = request.POST.get('senha2')

    if not nome or not cpf or not sexo or not email or not senha or not senha2:
        messages.error(request, 'Todos os campos devem ser preenchidos')
        return render(request, 'accounts/cadastro.html')

    return render(request, 'accounts/cadastro.html')
def dashboard(request):
    return render(request, 'accounts/dashboard.html')
