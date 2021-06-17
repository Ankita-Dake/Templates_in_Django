from django.http import HttpResponse
from django.shortcuts import render


def index(request):
    return render(request, 'home.html')


def log(request):
    return render(request, 'login.html')


def about(request):
    return render(request, 'about.html')


def contact(request):
    return (request, 'contact.html')
