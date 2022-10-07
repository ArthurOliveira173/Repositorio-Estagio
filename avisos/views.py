from django.shortcuts import render, get_object_or_404
from .models import Avisos
from django.contrib import messages
from django.core.paginator import Paginator
def index(request):
    avisos = Avisos.objects.all()
    paginator = Paginator(avisos, 10)

    page = request.GET.get('p')
    avisos = paginator.get_page(page)
    return render(request, 'avisos/index.html', {
        'avisos' : avisos
    })

def aviso(request, aviso_id):
    aviso = get_object_or_404(Avisos, avi_id=aviso_id)
    return render(request, 'avisos/aviso.html', {
        'aviso' : aviso
    })
