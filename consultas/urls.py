from django.shortcuts import render
from django.urls import path
from . import views

urlpatterns = [
    path('<int:id>/', views.consultas, name='consultas'),
     path('gravacao/<int:id>', views.gravacao, name='gravacao'),
]

# Create your views here.
