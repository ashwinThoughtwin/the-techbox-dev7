from django.shortcuts import render, HttpResponseRedirect
from django.contrib.auth.decorators import login_required
from django.contrib.auth import login, logout, authenticate
from django.urls import reverse
from django.http import HttpResponse
from .forms import LoginForm
# Create your views here.

def login_user(request):
    form = LoginForm()
    if request.method == "POST":
        form = LoginForm(data=request.POST)
        if form.is_valid():
            username = form.cleaned_data.get("username")
            password = form.cleaned_data.get("password")

            user = authenticate(username=username, password=password)

            if user is not None:
                login(request, user)
                return HttpResponse("You are Logged In Successfully.")

    return render(request, "app_auth/login.html", context={'form': form})


@login_required
def logout_user(request):
    logout(request)
    return HttpResponse("Logged Out")