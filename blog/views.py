from django.shortcuts import render
from blog.data import post

def blog(request):
    print('home')

    context = {
        'texto' : 'blog modificado pelo context',
        'posts' : post
    }
    return render(
        request,
        'blog/index.html',
        context,


    )



def example(request):
    print('example html1')
    context = {
        'texto' : 'example modificado pelo context'
    }

    return render(
        request,
        'blog/example.html',
        context
    )

# Create your views here.
