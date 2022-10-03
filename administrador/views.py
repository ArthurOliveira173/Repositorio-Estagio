import sys

from django.shortcuts import render
from django.apps import apps
alunoModel = apps.get_model("contas", "AlunoPcd")


# Create your views here.
from django.http import HttpResponse

def index(request):
    return render(request, 'administrador/index.html')

def homologar(request):
    return render(request, 'administrador/homologar.html')

def adminAlunos(request):
    alunos = alunoModel.objects.all()
    context = {
        'alunos': alunos
    }
    return render(request, 'administrador/alunos.html', context)

def adminMonitorTutor(request):
    return render(request, 'administrador/monitorTutor.html')

def adminInterpretes(request):
    return render(request, 'administrador/interpretes.html')

