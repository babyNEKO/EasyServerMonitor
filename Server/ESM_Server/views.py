from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.contrib.auth import logout
from django.contrib.auth import authenticate, login
from django.contrib import messages
from .models import ESM
from django.views.decorators.http import require_http_methods
from .Plugin.get_host_info import get_info


@require_http_methods(['GET'])
def index(request):
    pin_host = ESM.objects.all().filter(pin_to_index__exact=True)
    if pin_host.exists() is not False:
        context = {
            'index_host': pin_host,
            'host_info': [],
        }
        for i in pin_host:
            context['host_info'].append(get_info(ip_address=i.ip_address, port=i.client_port))
        return render(request=request, template_name='index.html', context=context)
    else:
        get_all_host = ESM.objects.all()
        context = {
            'index_host': get_all_host,
        }
        return render(request=request, template_name='index.html', context=context)


@login_required
def host_list(request):
    all_host = ESM.objects.all()
    context = {
        'all_host': all_host,
    }
    return render(request=request, template_name='host_list.html', context=context)


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
