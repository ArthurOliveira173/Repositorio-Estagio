from django.shortcuts import render, get_object_or_404, redirect
from django.http import Http404
from .models import Acompanhamentos, AcompanhamentoMonitores, AcompanhamentoTutores
from django.http import HttpResponseRedirect
from django.db.models import Q
from django.core.paginator import Paginator
from .forms import AcompanhamentosForm

# def handle_uploaded_file(f):
#     with open('avisos/uploads/'+f.name, 'wb+') as destination:
#         for chunk in f.chunks():
#             destination.write(chunk)
def acoIndex(request):
    acompanhamentos = Acompanhamentos.objects.order_by('-aco_id')
    paginator = Paginator(acompanhamentos, 10)

    page = request.GET.get('p')
    acompanhamentos = paginator.get_page(page)
    return render(request, 'acompanhamentos/acoIndex.html', {
        'acompanhamentos': acompanhamentos
    })

def adicionarAcompanhamento(request):
    submitted = False

    context = {}
    if request.POST:
        form = AcompanhamentosForm(request.POST, request.FILES)
        if form.is_valid():
            # handle_uploaded_file(request.FILES["avi_arquivos"])
            form.save()
            return HttpResponseRedirect('adicionarAcompanhamento?submitted=True')
        else:
            form = AcompanhamentosForm()
            form.save()
            return HttpResponseRedirect('adicionarAcompanhamento?submitted=True')
    else:
        form = AcompanhamentosForm()
        if 'submitted' in request.GET:
            submitted = True
    context['form'] = form
    context['submitted'] = submitted
    return render(request, 'acompanhamentos/adicionarAcompanhamento.html', context)

def acompanhamento(request, acompanhamento_id):
    acompanhamento = get_object_or_404(Acompanhamentos, aco_id=acompanhamento_id)
    try:
        monitoria = get_object_or_404(AcompanhamentoMonitores, AsMon_acompanhamento=acompanhamento)
    except:
        monitoria = None
    try:
        tutoria = get_object_or_404(AcompanhamentoTutores, AsTut_acompanhamento=acompanhamento)
    except:
        tutoria = None

    return render(request, 'acompanhamentos/acompanhamento.html', {
        'acompanhamento': acompanhamento,
        'monitoria': monitoria,
        'tutoria': tutoria
    })

def atualizarAcompanhamento(request, acompanhamento_id):
    acompanhamento = get_object_or_404(Acompanhamentos, aco_id=acompanhamento_id)

    form = AcompanhamentosForm(request.POST or None, instance=acompanhamento)
    if form.is_valid():
        form.save()
        return redirect('acoIndex')

    return render(request, 'acompanhamentos/atualizarAcompanhamento.html', {
        'acompanhamento': acompanhamento,
        'form': form
    })

def buscarAcompanhamento(request):
    if request.POST:
        searched = request.POST.get('searched')
        if searched:
            acompanhamentos = Acompanhamentos.objects.order_by('-aco_id').filter(
                Q(aco_semestre__icontains=searched) | Q(aco_aluno_pcd__alu_nome__icontains=searched)
            )
        else:
            acompanhamentos = None

        return render(request, 'acompanhamentos/buscarAcompanhamento.html', {
            'searched': searched,
            'acompanhamentos': acompanhamentos
        })
    else:
        return render(request, 'acompanhamentos/buscarAcompanhamento.html', {

        })
