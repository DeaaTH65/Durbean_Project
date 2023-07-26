from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User
from django.contrib import messages


# Create your views here.
def home(request):
    return render(request, 'home.html')


def loginPage(request):
    pass


def logoutUser(request):
    logout(request)
    messages.success(request, ("You have been logged out.!"))
    return redirect('home')


def registerPage(request):
    pass
