from django.shortcuts import render, redirect
from razer_project.models import Project, UserProject

def index(request):
    projects = Project.objects.all()
    context = {
        'title_name': 'Index',
        'projects': projects,
    }
    return render(request, 'index.html', context)

def about(request):
    if request.method == 'POST':
        name = request.POST['name']
        email = request.POST['email']
        description = request.POST['description']
        userproject = UserProject.objects.create(
            name=name,
            email=email,
            description=description
        )
        userproject.save()
        return redirect('about')

    context = {
        'title_name': 'About',
    }
    return render(request, 'about.html', context)