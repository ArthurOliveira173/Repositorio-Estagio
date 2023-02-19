import os
from django.shortcuts import render, get_object_or_404, redirect
from django.http import Http404, HttpResponse
from .models import Avisos
from django.http import HttpResponseRedirect
from django.db.models import Q
from django.core.paginator import Paginator
from django.contrib import messages
from .forms import AvisosForm
from membros.models import AlunoPcd, Administrador
import mimetypes
import pickle

# def handle_uploaded_file(f):
#     with open('avisos/uploads/'+f.name, 'wb+') as destination:
#         for chunk in f.chunks():
#             destination.write(chunk)

def baixar(request, filename):
    BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
    filename = str(filename)
    filepath = BASE_DIR + '\\uploads\\' + filename
    path = open(filepath, 'rb')
    mime_type, _ = mimetypes.guess_type(filepath)
    response = HttpResponse(path, content_type=mime_type)
    response['Content-Disposition'] = "attachment; filename=%s" % filename
    return response

def aviIndex(request):
    avisos = Avisos.objects.order_by('-avi_id').filter(
        avi_mostrar = True
    )
    paginator = Paginator(avisos, 10)

    page = request.GET.get('p')
    avisos = paginator.get_page(page)
    return render(request, 'avisos/aviIndex.html', {
        'avisos': avisos
    })

def aviIndexAluno(request):
    avisos = Avisos.objects.order_by('-avi_id').filter(
        avi_mostrar = True
    )
    aluno = get_object_or_404(AlunoPcd, alu_id=1)

    paginator = Paginator(avisos, 10)

    page = request.GET.get('p')
    avisos = paginator.get_page(page)
    return render(request, 'avisos/aviIndexAluno.html', {
        'avisos': avisos,
        'aluno': aluno
    })

def adicionarAviso(request):
    submitted = False

    context = {}
    if request.POST:
        form = AvisosForm(request.POST, request.FILES)
        if form.is_valid():
            # handle_uploaded_file(request.FILES["avi_arquivos"])
            avisoForm = form.save(commit=False)
            administrador = get_object_or_404(Administrador, adm_cpf=request.user.username)
            avisoForm.avi_administrador = administrador
            avisoForm.save()
            return HttpResponseRedirect('adicionarAviso?submitted=True')
        else:
            form = AvisosForm()

            messages.error("As informações inseridas são inválidas! Tente novamente.")
    else:
        form = AvisosForm()
        if 'submitted' in request.GET:
            submitted = True
    context['form'] = form
    context['submitted'] = submitted
    return render(request, 'avisos/adicionarAviso.html', context)

def buscarAviso(request):
    if request.POST:
        searched = request.POST.get('searched')
        if searched:
            avisos = Avisos.objects.order_by('-avi_id').filter(Q(avi_titulo__icontains=searched) | Q(avi_descricao__icontains=searched) )
        else:
            avisos = None

        return render(request, 'avisos/buscarAviso.html', {
            'searched': searched,
            'avisos': avisos
        })
    else:
        return render(request, 'avisos/buscarAviso.html', {

        })

def aviso(request, aviso_id):
    aviso = get_object_or_404(Avisos, avi_id=aviso_id)
    if not aviso.avi_mostrar:
        raise Http404()

    return render(request, 'avisos/aviso.html', {
        'aviso': aviso
    })

def atualizarAviso(request, aviso_id):
    aviso = get_object_or_404(Avisos, avi_id=aviso_id)
    if not aviso.avi_mostrar:
        raise Http404()

    form = AvisosForm(request.POST or None, instance=aviso)
    if form.is_valid():
        if form.cleaned_data['avi_arquivos']:
            arquivo = form.cleaned_data['avi_arquivos']
            arquivo_nome = str(arquivo)

            BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
            filepath = BASE_DIR + '\\uploads\\' + arquivo_nome

            with open(filepath, 'wb') as f:
                pickle.dump(arquivo, f)
        form.save()
        return redirect('aviIndex')

    return render(request, 'avisos/atualizarAviso.html', {
        'aviso': aviso,
        'form': form
    })

def deletarAviso(request, aviso_id):
    aviso = get_object_or_404(Avisos, avi_id=aviso_id)
    arquivo_nome = aviso.avi_arquivos
    BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
    filepath = BASE_DIR + '\\uploads\\' + str(arquivo_nome)
    aviso.delete()
    os.remove(filepath)
    return redirect('aviIndex')



#ALUNO

def aviIndexAluno(request):
    avisos = Avisos.objects.order_by('-avi_id').filter(
        avi_mostrar = True
    )
    paginator = Paginator(avisos, 10)

    page = request.GET.get('p')
    avisos = paginator.get_page(page)
    return render(request, 'avisos/aviIndexAluno.html', {
        'avisos': avisos
    })

def avisoAluno(request, aviso_id):
    aviso = get_object_or_404(Avisos, avi_id=aviso_id)
    if not aviso.avi_mostrar:
        raise Http404()

    return render(request, 'avisos/avisoAluno.html', {
        'aviso': aviso
    })


def buscarAvisoAluno(request):
    if request.POST:
        searched = request.POST.get('searched')
        if searched:
            avisos = Avisos.objects.order_by('-avi_id').filter(Q(avi_titulo__icontains=searched) | Q(avi_descricao__icontains=searched) )
        else:
            avisos = None

        return render(request, 'avisos/buscarAvisoAluno.html', {
            'searched': searched,
            'avisos': avisos
        })
    else:
        return render(request, 'avisos/buscarAvisoAluno.html', {

        })

def avisoAluno(request, aviso_id):
    aviso = get_object_or_404(Avisos, avi_id=aviso_id)
    if not aviso.avi_mostrar:
        raise Http404()

    return render(request, 'avisos/avisoAluno.html', {
        'aviso': aviso
    })
