from django.shortcuts import render

def blog(request):
    print('home')
    context = {
        'texto' : 'blog modificado pelo context'
    }
    return render(
        request,
        'blog/index.html',
        context
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
