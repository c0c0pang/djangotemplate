from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout

# Create your views here.


def main_view(request):
    if request.method == "POST":
        username = request.POST["username"]
        password = request.POST["password"]
        user = authenticate(username=username, password=password)
        if user is not None:
            print("인증성공")
            login(request, user)
            return render(request, "home.html")
        else:
            print("인증실패")

    return render(request, "users/main.html")


def login_view(request):
    return render(request, "users/login.html")


def logout_view(request):
    logout(request)
    return redirect("user:login")


def signup_view(request):
    return render(request, "users/signup.html")
