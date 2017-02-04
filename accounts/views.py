from django.contrib.auth import authenticate, get_user_model, login, logout
from django.shortcuts import render

from .forms import UserLoginForm


def login_view(request):
    form = UserLoginForm(request.POST or None)

    if form.is_valid():
        username = form.cleaned_data.get("username")
        password = form.cleaned_data.get("password")
        user = authenticate(username=username, password=password)
        login(request, user)

    return render(request, "form.html", {
        "form": form,
        "title": "Login",
    })


def register_view(request):
    return render(request, "form.html", {})


def logout_view(request):
    logout(request)
    return render(request, "form.html", {})