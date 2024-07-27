from django.shortcuts import render, redirect
from .models import Users
from django.contrib.auth.hashers import make_password, check_password
from django.contrib.auth import login as auth_login

def login(request):
    if request.method == 'POST':
        email = request.POST['email']
        password = request.POST['password']
        try:
            user = Users.objects.get(email=email)
            if check_password(password,user.password):
                auth_login(request,user)
                return redirect('home')
            else:
                return render(request,'login.html',{'error':'Invalid password'})
        except Users.DoesNotExist:
            return render(request, 'login.html',{'error':'Email does not exist'})
    else:
        return render(request, 'login.html')

def register(request):
    if request.method == 'POST':
        uname = request.POST['username']
        email = request.POST['email']
        password = request.POST['password']
        hashed_password = make_password(password)
        user = Users(uname=uname,email=email, password=hashed_password)
        user.save()
        return redirect('login')
    else:
        return render(request, 'register.html')

def home_view(request):
    return render(request,'home.html')
# Create your views here.
