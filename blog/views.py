# from django.shortcuts import render
from django.http import HttpResponse

def blog(request):
    print('Blog')
    return HttpResponse("blog do app1")


def example(request):
    print('example')
    return HttpResponse("examplo do app1")

# Create your views here.
