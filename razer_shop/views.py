from django.shortcuts import render

# Create your views here.
def shop(request):
    context = {
        'title_name': 'Shop'
    }
    return render(request, 'shop/shop.html', context)