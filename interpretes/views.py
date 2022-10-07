from django.shortcuts import render, get_object_or_404
from .models import Interprete
from django.core.paginator import Paginator
# Create your views here.
def index(request):
    interpretes = Interprete.objects.all()
    paginator = Paginator(interpretes, 10)

    page = request.GET.get('p')
    interpretes = paginator.get_page(page)
    return render(request, 'interpretes/index.html', {
        'interpretes' : interpretes
    })

def interprete(request, interprete_id):
    interprete = get_object_or_404(Interprete, int_id=interprete_id)
    return render(request, 'interpretes/interprete.html', {
        'interprete' : interprete
    })