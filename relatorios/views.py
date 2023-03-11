import os
from django.shortcuts import render, get_object_or_404, redirect
from django.http import Http404, HttpResponse
from django.http import HttpResponseRedirect
from django.db.models import Q
from django.core.paginator import Paginator
from django.contrib import messages
from .models import RelatoriosMon, RelatoriosTut
from .forms import RelatoriosMonForm, RelatoriosTutForm
from acompanhamentos.models import AcompanhamentoTutores, AcompanhamentoMonitores
from membros.models import Monitor, Tutor, CustomUser
import mimetypes

def baixarFileRelatorio(request, filename):
    BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
    filename = str(filename)
    filepath = BASE_DIR + '\\uploads\\' + filename
    path = open(filepath, 'rb')
    mime_type, _ = mimetypes.guess_type(filepath)
    response = HttpResponse(path, content_type=mime_type)
    response['Content-Disposition'] = "attachment; filename=%s" % filename
    return response

#ADMIN==============================================================================================

def relMIndex(request):
    relatoriosM = RelatoriosMon.objects.order_by('-relM_id')
    paginator = Paginator(relatoriosM, 10)

    page = request.GET.get('p')
    relatoriosM = paginator.get_page(page)
    return render(request, 'relatorios/relMIndex.html', {
        'relatoriosM': relatoriosM
    })

def relTIndex(request):
    relatoriosT = RelatoriosTut.objects.order_by('-relT_id')
    paginator = Paginator(relatoriosT, 10)

    page = request.GET.get('p')
    relatoriosT = paginator.get_page(page)
    return render(request, 'relatorios/relTIndex.html', {
        'relatoriosT': relatoriosT
    })

def relatorioM(request, relatorioM_id):
    relatorioM = get_object_or_404(RelatoriosMon, relM_id=relatorioM_id)

    return render(request, 'relatorios/relatorioM.html', {
        'relatorioM': relatorioM
    })

def relatorioT(request, relatorioT_id):
    relatorioT = get_object_or_404(RelatoriosTut, relT_id=relatorioT_id)

    return render(request, 'relatorios/relatorioT.html', {
        'relatorioT': relatorioT
    })

def buscarRelatorioM(request):
    if request.POST:
        searched = request.POST.get('searched')
        if searched:
            relatoriosM = RelatoriosMon.objects.order_by('-relM_id').filter(Q(relM_titulo__icontains=searched))
        else:
            relatoriosM = None

        return render(request, 'relatorios/buscarRelatorioM.html', {
            'searched': searched,
            'relatoriosM': relatoriosM
        })
    else:
        return render(request, 'relatorios/buscarRelatorioM.html', {

        })

def buscarRelatorioT(request):
    if request.POST:
        searched = request.POST.get('searched')
        if searched:
            relatoriosT = RelatoriosTut.objects.order_by('-relT_id').filter(Q(relT_titulo__icontains=searched))
        else:
            relatoriosT = None

        return render(request, 'relatorios/buscarRelatorioT.html', {
            'searched': searched,
            'relatoriosT': relatoriosT
        })
    else:
        return render(request, 'relatorios/buscarRelatorioT.html', {

        })

def deletarRelatorioM(request, relM_id):
    relatorioM = get_object_or_404(RelatoriosMon, relM_id=relM_id)
    arquivo_nome = relatorioM.relM_arquivo
    BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
    filepath = BASE_DIR + '\\uploads\\' + str(arquivo_nome)
    relatorioM.delete()
    os.remove(filepath)
    return redirect('relMIndex')

def deletarRelatorioT(request, relT_id):
    relatorioT = get_object_or_404(RelatoriosMon, relT_id=relT_id)
    arquivo_nome = relatorioT.relT_arquivo
    BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
    filepath = BASE_DIR + '\\uploads\\' + str(arquivo_nome)
    relatorioT.delete()
    os.remove(filepath)
    return redirect('relTIndex')

#MONITOR_TUTOR======================================================================================

def ajudaVerificadoM(request):
    user = request.user
    messages.success(request, "O relatório ja foi verificado por um administrador. Alterações não podem ser realizadas.")
    return redirect('relMIndexMonitor', user.id)

def ajudaVerificadoT(request):
    user = request.user
    messages.success(request, "O relatório ja foi verificado por um administrador. Alterações não podem ser realizadas.")
    return redirect('relTIndexTutor', user.id)

def relMIndexMonitor(request, user_id):
    try:
        user = get_object_or_404(CustomUser, id=user_id)
        monitor = get_object_or_404(Monitor, mon_usuario=user)
        monitoria = get_object_or_404(AcompanhamentoMonitores, AsMon_monitor=monitor)
        relatoriosM = RelatoriosMon.objects.order_by('-relM_id').filter(
            relM_monitoria=monitoria
        )
        paginator = Paginator(relatoriosM, 10)

        page = request.GET.get('p')
        relatoriosM = paginator.get_page(page)
    except:
        relatoriosM = None
    return render(request, 'relatorios/relMIndexMonitor.html', {
        'relatoriosM': relatoriosM
    })

def relTIndexTutor(request, user_id):
    try:
        user = get_object_or_404(CustomUser, id=user_id)
        tutor = get_object_or_404(Tutor, tut_usuario=user)
        tutoria = get_object_or_404(AcompanhamentoTutores, AsTut_tutor=tutor)
        relatoriosT = RelatoriosTut.objects.order_by('-relT_id').filter(
            relT_tutoria=tutoria
        )
        paginator = Paginator(relatoriosT, 10)

        page = request.GET.get('p')
        relatoriosT = paginator.get_page(page)
    except:
        relatoriosT = None
    return render(request, 'relatorios/relTIndexTutor.html', {
        'relatoriosT': relatoriosT
    })

def adicionarRelatorioMonitor(request):
    user = request.user
    context = {}
    if request.POST:
        form = RelatoriosMonForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            messages.success(request, "Relatório enviado com sucesso!")
            return redirect('relMIndexMonitor', user.id)
        else:
            form = RelatoriosMonForm(request.POST)
            messages.error(request, "As informações inseridas são inválidas! Tente novamente.")

    else:
        form = RelatoriosMonForm()

    context['form'] = form
    return render(request, 'relatorios/adicionarRelatorioMonitor.html', context)

def adicionarRelatorioTutor(request):
    user = request.user
    context = {}
    if request.POST:
        form = RelatoriosTutForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            messages.success(request, "Relatório enviado com sucesso!")
            return redirect('relMIndexTutor', user.id)
        else:
            form = RelatoriosTutForm(request.POST)
            messages.error(request, "As informações inseridas são inválidas! Tente novamente.")

    else:
        form = RelatoriosTutForm()

    context['form'] = form
    return render(request, 'relatorios/adicionarRelatorioTutor.html', context)

def atualizarRelatorioM(request, relatorioM_id):
    user = request.user
    relatorioM = get_object_or_404(RelatoriosMon, relM_id=relatorioM_id)

    if request.method == 'POST':
        form = RelatoriosMonForm(request.POST or None, request.FILES, instance=relatorioM)
        if form.is_valid():
            form.save()
            return redirect('relMIndexMonitor', user.id)
    else:
        form = RelatoriosMonForm(instance=relatorioM)

    return render(request, 'relatorios/atualizarRelatorioM.html', {
        'relatorioM': relatorioM,
        'form': form
    })

def atualizarRelatorioT(request, relatorioT_id):
    user = request.user
    relatorioT = get_object_or_404(RelatoriosTut, relT_id=relatorioT_id)

    if request.method == 'POST':
        form = RelatoriosTutForm(request.POST or None, request.FILES, instance=relatorioT)
        if form.is_valid():
            form.save()
            return redirect('relTIndexTutor', user.id)
    else:
        form = RelatoriosTutForm(instance=relatorioT)

    return render(request, 'relatorios/atualizarRelatorioT.html', {
        'relatorioT': relatorioT,
        'form': form
    })

def buscarRelatorioMonitor(request, user_id):
    if request.POST:
        searched = request.POST.get('searched')
        if searched:
            try:
                user = get_object_or_404(CustomUser, id=user_id)
                monitor = get_object_or_404(Monitor, mon_usuario=user)
                monitoria = get_object_or_404(AcompanhamentoMonitores, AsMon_monitor=monitor)
                relatoriosM = RelatoriosMon.objects.order_by('-relM_id').filter(Q(relM_titulo__icontains=searched)).filter(relM_monitoria=monitoria)
            except:
                relatoriosM = None
        else:
            relatoriosM = None

        return render(request, 'relatorios/buscarRelatorioMonitor.html', {
            'searched': searched,
            'relatoriosM': relatoriosM
        })
    else:
        return render(request, 'relatorios/buscarRelatorioMonitor.html', {

        })

def buscarRelatorioTutor(request):
    if request.POST:
        searched = request.POST.get('searched')
        if searched:
            relatoriosT = RelatoriosTut.objects.order_by('-relT_id').filter(Q(relT_titulo__icontains=searched))
        else:
            relatoriosT = None

        return render(request, 'relatorios/buscarRelatorioT.html', {
            'searched': searched,
            'relatoriosT': relatoriosT
        })
    else:
        return render(request, 'relatorios/buscarRelatorioT.html', {

        })

def deletarRelatorioMonitor(request, relM_id):
    user = request.user
    relatorioM = get_object_or_404(RelatoriosMon, relM_id=relM_id)
    arquivo_nome = relatorioM.relM_arquivo
    BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
    filepath = BASE_DIR + '\\uploads\\' + str(arquivo_nome)
    relatorioM.delete()
    os.remove(filepath)
    return redirect('relMIndexMonitor', user.id)

def deletarRelatorioTutor(request, relT_id):
    user = request.user
    relatorioT = get_object_or_404(RelatoriosMon, relT_id=relT_id)
    arquivo_nome = relatorioT.relT_arquivo
    BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
    filepath = BASE_DIR + '\\uploads\\' + str(arquivo_nome)
    relatorioT.delete()
    os.remove(filepath)
    return redirect('relTIndexTutor', user.id)