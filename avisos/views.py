from django.shortcuts import render, get_object_or_404
from django.http import Http404
from .models import Avisos
from django.http import HttpResponseRedirect
from django.db.models import Q
from django.core.paginator import Paginator
from .forms import AvisosForm

# def handle_uploaded_file(f):
#     with open('avisos/uploads/'+f.name, 'wb+') as destination:
#         for chunk in f.chunks():
#             destination.write(chunk)
def index(request):
    avisos = Avisos.objects.order_by('-avi_id').filter(
        avi_mostrar = True
    )
    paginator = Paginator(avisos, 10)

    page = request.GET.get('p')
    avisos = paginator.get_page(page)
    return render(request, 'avisos/index.html', {
        'avisos': avisos
    })

def adicionarAviso(request):
    submitted = False

    context = {}
    if request.POST:
        form = AvisosForm(request.POST, request.FILES)
        if form.is_valid():
            # handle_uploaded_file(request.FILES["avi_arquivos"])
            form.save()
            return HttpResponseRedirect('adicionarAviso?submitted=True')
        else:
            form = AvisosForm()
            form.save()
            return HttpResponseRedirect('adicionarAviso?submitted=True')
    else:
        form = AvisosForm()
        if 'submitted' in request.GET:
            submitted = True
    context['form'] = form
    context['submitted'] = submitted
    return render(request, 'avisos/adicionarAviso.html', context)

def aviso(request, aviso_id):
    aviso = get_object_or_404(Avisos, avi_id=aviso_id)

    if not aviso.avi_mostrar:
        raise Http404()

    return render(request, 'avisos/aviso.html', {
        'aviso' : aviso
    })

def buscarAviso(request):
    if request.POST:
        searched = request.POST.get('searched')
        if searched:
            avisos = Avisos.objects.filter(Q(avi_titulo__icontains=searched) | Q(avi_descricao__icontains=searched) )
        else:
            avisos = None

        return render(request, 'avisos/buscarAviso.html', {
            'searched': searched,
            'avisos': avisos
        })
    else:
        return render(request, 'avisos/buscarAviso.html', {

        })
