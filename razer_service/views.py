from django.shortcuts import render, redirect
from django.contrib import messages
from razer_project.models import UserProject
from django.contrib.sites.shortcuts import get_current_site
from django.template.loader import render_to_string
from django.utils.http import urlsafe_base64_encode, urlsafe_base64_decode
from django.utils.encoding import force_bytes
from django.contrib.auth.tokens import default_token_generator
from django.core.mail import EmailMessage
from razer_project.models import Project, UserProject, Tag
from razer_blog.models import Blog

# Create your views here.


def service(request):
    if request.method == 'POST':
        name = request.POST['name']
        email = request.POST['email']
        description = request.POST['description']
        userproject = UserProject.objects.create(
            name=name,
            email=email,
            description=description
        )
        mail_subject = f'New Project Request - {description}'
        message = render_to_string('email/user_project.html', {
            'name': name,
            'email': email,
            'description': description
        })
        to_email = 'razermindstudio@gmail.com'
        send_email = EmailMessage(mail_subject, message, to=[to_email])
        if send_email.send():
            userproject.save()
            messages.success(
                request, 'You have successfully created a New Project request!')
    context = {
        'title_name': 'Service'
    }
    return render(request, 'service/service.html', context)
