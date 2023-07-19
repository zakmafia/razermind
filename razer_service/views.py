from django.shortcuts import render

# Create your views here.
def service(request):
    context = {
        'title_name': 'service'
    }
    return render(request, 'service/service.html', context)