from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from .models import Project, ProjectPhoto, Tag
from .forms import ProjectForm, ProjectImageForm
# Create your views here.


def project(request):
    projects = Project.objects.all()
    branding_tag = Tag.objects.filter(slug='branding')
    website_tag = Tag.objects.filter(slug='websites')
    social_media_tag = Tag.objects.filter(slug='social-media')
    projects_branding = Project.objects.filter(tags__in=branding_tag)
    projects_websites = Project.objects.filter(tags__in=website_tag)
    projects_social_media = Project.objects.filter(tags__in=social_media_tag)
    context = {
        'title_name': 'Project',
        'projects_branding': projects_branding,
        'projects_websites': projects_websites,
        'projects_social_media': projects_social_media,
        'projects': projects
    }
    return render(request, 'project/project.html', context)


def detail_project(request, p_id):
    project = get_object_or_404(Project, pk=p_id)
    # tags = Tag.objects.all()
    project_photos = ProjectPhoto.objects.filter(project=project.id)
    next_project = Project.objects.filter(created__gt=project.created).first()
    prev_project = Project.objects.filter(created__lt=project.created).last()
    context = {
        'project': project,
        'project_photos': project_photos,
        'title_name': 'Project',
        'next_project': next_project,
        'prev_project': prev_project,

    }
    return render(request, "project/detail_project.html", context)


def insert_project_image(request, p_id):
    project = Project.objects.get(id=p_id)
    if request.method == 'POST':
        form = ProjectImageForm(request.POST, request.FILES)
        if form.is_valid():
            for image in request.FILES.getlist('images'):
                ProjectPhoto.objects.create(images=image, project=project)
    else:
        form = ProjectImageForm()
    context = {
        'form': form
    }
    return render(request, "project/insert_project_img.html", context)
