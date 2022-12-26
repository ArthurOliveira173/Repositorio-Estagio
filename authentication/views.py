from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages

def authLogin(request):
    if request.method == "POST":
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('aviIndex')
        else:
            messages.success(request, "There was an error while Logging in, Please try again.")
            return redirect('authLogin')
    else:
        return render(request, 'authenticate/authLogin.html', {

        })

def authLogout(request):
    logout(request)
    messages.success(request, "You were Logged out!")
    return redirect('authLogin')
