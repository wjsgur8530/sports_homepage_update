import requests
from django.contrib import auth
from django.contrib.auth import authenticate
from django.shortcuts import render, redirect
from bs4 import BeautifulSoup
# Create your views here.
# 로그인
def login(request):
    if request.method == 'POST':
        username = request.POST['id']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user is not None:
            auth.login(request, user)
            return redirect('home')
        else:
            return render(request, 'login.html', {'error': 'username or password is incorrect.'})
    else:
        return render(request, 'login.html')


# 로그아웃
def logout(request):
    auth.logout(request)
    return redirect('login')