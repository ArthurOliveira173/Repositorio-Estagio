from django.shortcuts import render, get_object_or_404
from django.http import HttpResponseRedirect, Http404
from django.apps import apps
from django.core.paginator import Paginator
from django.db.models import Q
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
    if request.POST:
        searched = request.POST.get('searched')
        if searched:
            try:
                alunos = AlunoPcd.objects.filter(Q(alu_nome__icontains=searched) | Q(alu_curso__icontains=searched))
            except:
                alunos = AlunoPcd.objects.filter(Q(alu_nome__icontains=searched))
        else:
            alunos = None

        return render(request, 'administrador/buscarAluno.html', {
            'searched': searched,
            'alunos': alunos
        })
    else:
        return render(request, 'administrador/buscarAluno.html', {

        })


def aluno(request, aluno_id):
    aluno = get_object_or_404(AlunoPcd, alu_id=aluno_id)

    return render(request, 'administrador/aluno.html', {
        'aluno': aluno
    })

def adminMonitores(request):
    return render(request, 'administrador/monitores.html')

def adminTutores(request):
    return render(request, 'administrador/tutores.html')

def adminInterpretes(request):
    return render(request, 'administrador/interpretes.html')

