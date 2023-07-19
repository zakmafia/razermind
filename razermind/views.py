from django.shortcuts import render

def index(request):
    context = {
        'title_name': 'index'
    }
    return render(request, 'index.html', context)