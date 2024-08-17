from django.shortcuts import render
from blog.data import posts

def blog(request):
    print('blog')

    context = {
        'texto' : 'blog modificado pelo context',
        'posts' : posts
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



# Create your views here.
def post(request, id):
    print("post", id)

    context = {
        'texto' : 'blog modificado pelo context',
        'posts' : posts
    }
    return render(
        request,
        'blog/index.html',
        context,


    )