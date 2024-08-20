from django.shortcuts import render
from blog.data import posts
from typing import Any 
from django.http import HttpResponse, Http404

def blog(request):
    print('blog')

    context = {
        'texto' : 'Bem vindo a página do blog feito em Django!',
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
    return render(
        request,
        'blog/index.html',
        context
    )



# Create your views here.
def post(request: HttpResponse, post_id:int):

    found_post:dict[str, Any] | None = None
    for post in posts:
        if post['id'] == post_id:
            found_post = post #Aqui ajuda para o loop não ficar pecorrendo todos os id
            break

    if found_post is None:
        raise Http404("Esse Post não existe") # Aqui você pode importar o 404 para informar para o usuário a pág não encontrada
        

    context = {
        'post' : found_post,
        'titulo' : found_post['title'] + ' - ',
    }
    return render(
        request,
        'blog/post.html',
        context,


    )