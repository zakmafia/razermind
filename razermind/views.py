from django.shortcuts import render, redirect
from django.contrib import messages
# For about message
from django.contrib.sites.shortcuts import get_current_site
from django.template.loader import render_to_string
from django.utils.http import urlsafe_base64_encode, urlsafe_base64_decode
from django.utils.encoding import force_bytes
from django.contrib.auth.tokens import default_token_generator
from django.core.mail import EmailMessage
from razer_project.models import Project, UserProject, Tag
from razer_blog.models import Blog


def index(request):
    branding_tag = Tag.objects.filter(slug='branding')
    website_tag = Tag.objects.filter(slug='websites')
    social_media_tag = Tag.objects.filter(slug='social-media')
    projects_branding = Project.objects.filter(tags__in=branding_tag)
    projects_websites = Project.objects.filter(tags__in=website_tag)
    projects_social_media = Project.objects.filter(tags__in=social_media_tag)
    blogs = Blog.objects.all()

    context = {
        'title_name': 'Index',
        'projects_branding': projects_branding,
        'projects_websites': projects_websites,
        'projects_social_media': projects_social_media,
        'blogs': blogs,
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
        messages.success(
            request, 'You have successfully created a New Project request!')
    else:
        messages.error(
            request, 'Something went wrong!')
    context = {
        'title_name': 'About',
    }
    return render(request, 'about.html', context)
