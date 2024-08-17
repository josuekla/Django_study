from django.contrib import admin
from django.urls import path
from blog import views

app_name = 'blog'

urlpatterns = [
    path('', views.blog, name='home'), # aqui é como se começasse blog/
    path('post/<id>', views.post, name='post'),
    path('example/', views.example, name='example'),
]