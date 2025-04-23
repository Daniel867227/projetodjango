from django.http import HttpResponseRedirect
from django.urls import reverse
from django.contrib.auth import logout, authenticate
from django.contrib.auth import login as login_auth
from django.shortcuts import render
from django.contrib.auth.forms import UserCreationForm


def logout_view(request):
    """Faz o logout"""
    logout(request)
    return HttpResponseRedirect(reverse('index'))


def register(request):
    """Registra novo usuário"""
    if request.user.is_authenticated:
        return HttpResponseRedirect(reverse('index'))

    if request.method != 'POST':
        form = UserCreationForm()
    else:
        form = UserCreationForm(data=request.POST)
        if form.is_valid():
            new_user = form.save()
    context = {'form': form}
    return render(request, 'users/register.html', context)
