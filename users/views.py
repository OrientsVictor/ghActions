from django.shortcuts import render
from django.urls import reverse
from django.http import HttpResponseRedirect
from django.contrib.auth import authenticate, login as auth_login, logout as auth_logout


# Create your views here.
def index(request):
    if not request.user.is_authenticated:
        return HttpResponseRedirect(reverse("login"))
    return render(request, "users/index.html", {"request": request})


def login(request):
    if request.method == "POST":
        username = request.POST["username"]
        password = request.POST["password"]

        user = authenticate(username=username, password=password)

        if user:
            auth_login(request, user)
            return HttpResponseRedirect(reverse("index"))
        else:
            return render(
                request, "users/login.html", {"message": "Invalid Credentials"}
            )

    else:
        return render(request, "users/login.html")


def logout(request):
    auth_logout(request)
    return HttpResponseRedirect(reverse("login"))
