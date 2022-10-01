from django.shortcuts import render
from django.shortcuts import render, redirect
from django.contrib.auth import login, logout,authenticate
from django.views.generic import CreateView
from .models import AlunoPcd
from .forms import AlunoForms
# Create your views here.
def index(request):
    return render(request, 'alunos/index.html')

class forms(CreateView):

    model = AlunoPcd
    form_class = AlunoForms

    def form_valid(self, form):
        user = form.save()
        login(self.request, user)
        return redirect('alunos/index.html')