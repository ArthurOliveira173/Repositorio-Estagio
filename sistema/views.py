from django.shortcuts import render
from django.http import HttpResponse

def erro404(request):
    return render(request, 'sistema/erro404.html')