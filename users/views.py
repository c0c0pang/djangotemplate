import imp
from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from .models import User
from django.http import HttpResponse
from django.contrib.auth.hashers import make_password
# Create your views here.


def login_view(request):
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
    return render(request, "users/login.html")


def logout_view(request):
    logout(request)
    return redirect("/")


def signup_view(request):
    if request.method == "POST":
        username = request.POST["username"]
        password = request.POST["password"]
        re_password = request.POST["re_password"]
        email = request.POST["email"]
        res_data = {}
        if password != re_password:
            res_data['error'] = "비밀번호가 다름"
        else:
            user = User.objects.create_user(username, email, password)
            user.save()
            return redirect("user:login")

    return render(request, "users/signup.html")
