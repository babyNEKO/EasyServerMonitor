from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.contrib.auth import logout
from django.contrib.auth import authenticate, login
from django.contrib import messages
from models import ESM


# Create your views here.
def index(request):
    show_host = ESM.objects.all()
    return render(request=request, template_name='index.html')


@login_required
def add_host(request, ip_address=None):
    return render(request=request, template_name='add_host.html')


@login_required
def view_host(request, ip_address):
    return render(request=request, template_name='view_host.html')


def user_login(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(username=username, password=password)
        if user is not None:
            if user.is_active:
                login(request, user)
                return redirect('index')
            else:
                messages.error(request, '登陆失败')
        else:
            messages.error(request, '登录失败')
    return render(request=request, template_name='login.html')


def user_logout(request):
    if request.user.is_authenticated:
        logout(request=request)
        return redirect('index')
    else:
        return redirect('index')
