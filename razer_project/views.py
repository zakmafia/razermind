from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from .models import Project, ProjectPhoto
from .forms import ProjectForm
# Create your views here.
# @login_required(login_url='login')
# def upload_project(request):
#     form = ProjectForm()
#     if request.method == 'POST':
#         form = ProjectForm(request.POST, request.FILES)
#         if form.is_valid():
#             form.save()
#             return redirect('upload_project')

#     context = {'form': form}
#     return render(request, "project/upload_project.html", context)

def detail_project(request, p_id):
    project = Project.objects.get(id=p_id)
    project_photos = ProjectPhoto.objects.filter(project=project.id)
    context = {
        'project': project,
        'project_photos': project_photos,
        'title_name': 'Project'
    }
    return render(request, "project/project.html", context)