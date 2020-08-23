from django.shortcuts import render
from django.http import HttpResponse


def index(request):
    return render(request, 'index.html')

def home(request):
    return render(request, 'home.html')

def projects(request):
    return render(request, 'projects.html')

def project_1(request):
    return render(request, 'project_1.html')

def resume(request):
    return render(request, 'resume.html')

def certificates(request):
    return render(request, 'certificates.html')

def home(request):
    return render(request, 'home.html')
