from django.shortcuts import render, redirect, get_object_or_404
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
    project = get_object_or_404(Project, pk=p_id)
    project_photos = ProjectPhoto.objects.filter(project=project.id)
    next_project = Project.objects.filter(created__gt=project.created).first()
    prev_project = Project.objects.filter(created__lt=project.created).last()
    context = {
        'project': project,
        'project_photos': project_photos,
        'title_name': 'Project',
        'next_project': next_project,
        'prev_project': prev_project
    }
    return render(request, "project/project.html", context)