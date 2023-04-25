from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from django.http import HttpResponse
from . models import Button

# Create your views here.

def login_user(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('index')
        else:
            messages.success(request, 'There was an error, try again!')
            return redirect('login_user')
    else:
        return render(request, "login.html", { 'is_logged_in': request.user.is_authenticated })
    
def logout_user(request):
    logout(request)
    return redirect('login_user')
    
def index(request):
    if not request.user.is_authenticated:
        messages.success(request, 'You cannot access that without logging in!')
        return redirect('login_user')
    else:
        if not Button.objects.first().exists():
            Button.objects.create(state='False')
        return render(request, 'index.html', { 'is_logged_in': True, "Button": Button.objects.first()})