from django.shortcuts import render

def home(request):
    print('home')

    context = {
        'texto' : 'home modificado pelo context',
        'titulo' : 'Site django - '
    }

    return render(
        request,
        'home/index.html',
        context
    )

# Create your views here.
