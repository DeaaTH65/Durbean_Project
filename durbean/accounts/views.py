from django.shortcuts import render


# Create your views here.
def home(request):
    return render(request, 'home.html')


def loginPage(request):
    pass


def logoutUser(request):
    pass


def registerPage(request):
    pass
