from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth.views import login as auth_login
from django.urls import reverse as r
from django.http import HttpResponseRedirect
from django.shortcuts import render, redirect


def home(request):
    template_name = "core/index.html"
    if request.method == "POST":
        form = AuthenticationForm(request, data=request.POST)
        if form.is_valid():
            auth_login(request, form.get_user())
            return redirect('sistema_home')
    else:
        form = AuthenticationForm()
    context = {'form': form}
    return render(request, template_name, context)


def sistema(request):
    return render(request, 'core/sistema.html')
