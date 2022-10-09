from django.shortcuts import render, get_object_or_404
from django.http import Http404
from .models import Avisos
from django.contrib import messages
from django.core.paginator import Paginator
def index(request):
    avisos = Avisos.objects.order_by('-avi_id').filter(
        avi_mostrar = True
    )
    paginator = Paginator(avisos, 10)

    page = request.GET.get('p')
    avisos = paginator.get_page(page)
    return render(request, 'avisos/index.html', {
        'avisos' : avisos
    })

def aviso(request, aviso_id):
    aviso = get_object_or_404(Avisos, avi_id=aviso_id)

    if not aviso.avi_mostrar:
        raise Http404()

    return render(request, 'avisos/aviso.html', {
        'aviso' : aviso
    })
