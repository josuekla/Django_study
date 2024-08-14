from django.contrib import admin
from django.urls import path
from blog import views

urlpatterns = [
    path('', views.blog), # aqui é como se começasse blog/
    path('example/', views.example)
]