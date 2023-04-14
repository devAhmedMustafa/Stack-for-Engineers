from django.shortcuts import render, redirect
from .forms import NewUserForm
from django.http import JsonResponse
from django.contrib.auth import login as auth_login, authenticate, logout as auth_logout
from django.contrib.auth.models import User

def sign_up(request):

    if request.method == 'POST':
        form = NewUserForm(request.POST)
        if form.is_valid():
            user = form.save()
            auth_login(request, user)
            return redirect('home') 
    form = NewUserForm()
    return render(request, 'sign_up.html', {'form':form})

def login(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(request, username=username, password=password)
        if user is not None:
            auth_login(request, user)
            return redirect('home')
        else:
            return render(request, 'login.html', {'error': 'username or password is incorrect'})
        
    else:
        return render(request, 'login.html')


def logout(request):
    auth_logout(request)
    return redirect('home')

def user_validation(request):

    data = {
        'is_taken': User.objects.filter(username=request.GET.get('username')).exists()
    }

    return JsonResponse(data)