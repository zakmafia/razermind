from django.shortcuts import render, get_object_or_404
from django.contrib import messages
# for blog comment
from django.contrib.sites.shortcuts import get_current_site
from django.template.loader import render_to_string
from django.utils.http import urlsafe_base64_encode, urlsafe_base64_decode
from django.utils.encoding import force_bytes
from django.contrib.auth.tokens import default_token_generator
from django.core.mail import EmailMessage

from .models import Blog, BlogComment
# Create your views here.


def blog(request):
    blogs = Blog.objects.all()
    context = {
        'title_name': 'Blog',
        'blogs': blogs
    }
    return render(request, "blog/blog.html", context)


def detail_blog(request, b_id):
    blog = get_object_or_404(Blog, pk=b_id)
    next_blog = Blog.objects.filter(created__gt=blog.created).first()
    prev_blog = Blog.objects.filter(created__lt=blog.created).last()

    if request.method == 'POST':
        name = request.POST['name']
        email = request.POST['email']
        comment = request.POST['comment']
        usercomment = BlogComment.objects.create(
            name=name,
            email=email,
            comment=comment,
            blog=blog
        )
        mail_subject = f'New Comment for blog - {blog.title}'
        message = render_to_string('email/blog_comment.html', {
            'name': name,
            'email': email,
            'comment': comment,
            'title': blog.title
        })
        to_email = 'razermindstudio@gmail.com'
        send_email = EmailMessage(mail_subject, message, to=[to_email])
        if send_email.send():
            usercomment.save()
            messages.success(
                request, 'You have successfully commented on this blog article!')
    context = {
        'blog': blog,
        'title_name': 'Blog',
        'next_blog': next_blog,
        'prev_blog': prev_blog
    }

    return render(request, "blog/detail_blog.html", context)
