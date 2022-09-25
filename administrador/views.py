from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse

def index(request):
    return render(request, 'administrador/index.html')

def homologar(request):
    return render(request, 'administrador/homologar.html')
