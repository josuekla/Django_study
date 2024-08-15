from django.contrib import admin
from django.urls import path
from home import views #no lugar do home pode ser aplicado o "." --> pasta raíz

urlpatterns = [
    path('', views.home),   
]