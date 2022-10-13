from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse
from .models import Monitor, Tutor
from django.core.paginator import Paginator
def index_mon(request):
    monitores = Monitor.objects.all()
    paginator = Paginator(monitores, 10)

    page = request.GET.get('p')
    monitores = paginator.get_page(page)
    return render(request, 'monitor_tutor/index_mon.html', {
        'monitores' : monitores
    })

def monAluno(request):
    return render(request, 'monitor_tutor/monAluno.html')

def monitor(request, monitor_id):
    monitor = get_object_or_404(Monitor, mon_id=monitor_id)
    return render(request, 'monitor_tutor/monitor.html', {
        'monitor' : monitor
    })

def index_tut(request):
    tutores = Tutor.objects.all()
    paginator = Paginator(tutores, 10)

    page = request.GET.get('p')
    tutores = paginator.get_page(page)
    return render(request, 'monitor_tutor/index_tut.html', {
        'tutores' : tutores
    })

def tutAluno(request):
    return render(request, 'monitor_tutor/tutAluno.html')

def tutor(request, tutor_id):
    tutor = get_object_or_404(Tutor, tut_id=tutor_id)
    return render(request, 'monitor_tutor/tutor.html', {
        'tutor' : tutor
    })