from django.shortcuts import render, get_object_or_404
from .models import Interprete
from django.core.paginator import Paginator
# Create your views here.
def intIndex(request):
    interpretes = Interprete.objects.all()
    paginator = Paginator(interpretes, 10)

    page = request.GET.get('p')
    interpretes = paginator.get_page(page)
    return render(request, 'interpretes/intIndex.html', {
        'interpretes' : interpretes
    })

def intAluno(request):
    return render(request, 'interpretes/intAluno.html')

def interprete(request, interprete_id):
    interprete = get_object_or_404(Interprete, int_id=interprete_id)
    return render(request, 'interpretes/interprete.html', {
        'interprete' : interprete
    })