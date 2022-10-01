from django.contrib.auth.forms import AuthenticationForm
from django.shortcuts import render
from django.contrib import messages
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

def login_user(request):
    if request.method=='POST':
        form = AuthenticationForm(data=request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            user = authenticate(username=username, password=password)
            if user is not None :
                login(request,user)
                return redirect('alunos/index.html')
            else:
                messages.error(request,"Invalid username or password")
        else:
            messages.error(request,"Invalid username or password")
    return render(request, 'alunos/login.html',context={'form':AuthenticationForm()})

def logout_user(request):
    logout(request)
    return redirect('alunos/login.html')