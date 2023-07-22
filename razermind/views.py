from django.shortcuts import render
from razer_project.models import Project

def index(request):
    projects = Project.objects.all()
    context = {
        'title_name': 'Index',
        'projects': projects,
    }
    return render(request, 'index.html', context)

def about(request):
    context = {
        'title_name': 'About'
    }
    return render(request, 'about.html', context)