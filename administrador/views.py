from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse

def index(request):
    return render(request, 'administrador/index.html')

def homologar(request):
    return render(request, 'administrador/homologar.html')

def adminAlunos(request):
    return render(request, 'administrador/alunos.html')

def adminMonitorTutor(request):
    return render(request, 'administrador/monitorTutor.html')

def adminInterpretes(request):
    return render(request, 'administrador/interpretes.html')

