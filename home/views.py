# from django.shortcuts import render
from django.http import HttpResponse

def home(request):
    print('home')
    return HttpResponse("home do app1")

# Create your views here.
