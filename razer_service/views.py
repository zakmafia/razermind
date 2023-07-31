from django.shortcuts import render, redirect
# Create your views here.


def service(request):
    context = {
        'title_name': 'Service'
    }
    return render(request, 'service/service.html', context)
