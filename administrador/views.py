from django.shortcuts import render
from django.http import HttpResponseRedirect
from django.apps import apps
from django.core.paginator import Paginator
from alunos.models import AlunoPcd
from alunos.forms import AlunosForm


# Create your views here.
from django.http import HttpResponse

def index(request):
    return render(request, 'administrador/index.html')

def homologar(request):
    return render(request, 'administrador/homologar.html')

def adminAlunos(request):
    alunos = AlunoPcd.objects.all()

    paginator = Paginator(alunos, 10)
    page = request.GET.get('p')
    alunos = paginator.get_page(page)

    return render(request, 'administrador/alunos.html', {
        'alunos': alunos
    })

def adicionarAluno(request):
    submitted = False

    context = {}
    if request.POST:
        form = AlunosForm(request.POST)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect('adicionarAluno?submitted=True')
        else:
            form = AlunosForm()
            form.save()
            return HttpResponseRedirect('adicionarAluno?submitted=True')
    else:
        form = AlunosForm()
        if 'submitted' in request.GET:
            submitted = True
    context['form'] = form
    context['submitted'] = submitted
    return render(request, 'administrador/adicionarAluno.html', context)


def buscarAluno(request):
    return render(request, 'administrador/alunos.html', {

    })


def aluno(request):
    return render(request, 'administrador/alunos.html', {

    })

def adminMonitorTutor(request):
    return render(request, 'administrador/monitorTutor.html')

def adminInterpretes(request):
    return render(request, 'administrador/interpretes.html')

