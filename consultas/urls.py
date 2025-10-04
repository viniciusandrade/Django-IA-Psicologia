from django.shortcuts import render
from django.urls import path
from . import views

urlpatterns = [
    path('<int:id>/', views.consultas, name='consultas'),
]

# Create your views here.
