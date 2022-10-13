from django.shortcuts import render
from django.contrib import messages
from django.shortcuts import render, get_object_or_404
from django.contrib.auth import login, logout,authenticate
from django.views.generic import CreateView
from .models import AlunoPcd
from django.core.paginator import Paginator
# Create your views here.
def index(request):
    alunos = AlunoPcd.objects.all()
    paginator = Paginator(alunos, 10)

    page = request.GET.get('p')
    alunos = paginator.get_page(page)

    return render(request, 'alunos/index.html', {
     'alunos' : alunos
    })

def acompanhantes(request):
    return render(request, 'alunos/acompanhantes.html')

def aluno(request, aluno_id):
    aluno = get_object_or_404(AlunoPcd, alu_id=aluno_id)
    return render(request, 'alunos/aluno.html', {
        'aluno' : aluno
    })
