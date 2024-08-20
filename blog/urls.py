from django.contrib import admin
from django.urls import path
from blog import views

app_name = 'blog'

urlpatterns = [
    path('', views.blog, name='home'), # aqui é como se começasse blog/
    path('<int:post_id>/', views.post, name='post'), 
    path('example/', views.example, name='example'),
]


#Boas práticas: Sempre colocar uma barra / depois dos links. organizar sos links de mais específica.