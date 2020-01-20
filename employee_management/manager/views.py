from django.http import HttpResponse
from django.shortcuts import render,redirect
from django.contrib.auth.models import User
from django.contrib import auth
from .forms import *

# Create your views here.
def home(request):
  return render(request,'base.html')


#Function For Register/Signup
def register(request):
    if request.method == 'POST':
        # User has info and wants an account now!
        if request.POST['password1'] == request.POST['password2']:
            try:
                user = User.objects.get(email=request.POST['email'])
                return render(request, 'register.html', {'error':'Email has already been taken'})
            except User.DoesNotExist:
                user = User.objects.create_user(request.POST['email'], password=request.POST['password1'])
                auth.login(request,user)
                return redirect('home')
        else:
            return render(request, 'register.html', {'error':'Passwords must match'})
    else:
        # User wants to enter info
        return render(request, 'register.html')

#Function for login
def login(request):
    if request.method == 'POST':
        user = auth.authenticate(email=request.POST['email'],password=request.POST['password'])
        if user is not None:
            auth.login(request, user)
            return redirect('employee')
        else:
            return render(request, 'login.html',{'error':'email or password is incorrect.'})
    else:
        return render(request, 'login.html')

#Function for logout
def logout(request):
    # if request.method == 'POST':
    #     auth.logout(request)
        return render(request,'base.html')