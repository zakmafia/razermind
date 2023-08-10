from django.shortcuts import render, get_object_or_404
from django.contrib import messages
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
        usercomment.save()
        messages.success(
            request, 'You have successfully commented on this blog article!')
    else:
        messages.error(
            request, 'Something went wrong!')

    context = {
        'blog': blog,
        'title_name': 'Blog',
        'next_blog': next_blog,
        'prev_blog': prev_blog
    }

    return render(request, "blog/detail_blog.html", context)
