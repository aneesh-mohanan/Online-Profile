from django.urls import path
from . import  views

urlpatterns = [
    path('', views.index),
    path('projects', views.projects),
    path('resume', views.resume),
    path('certificates', views.certificates),
    path('home', views.home),
    path('projects', views.projects),
]