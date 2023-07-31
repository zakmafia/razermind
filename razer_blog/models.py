import uuid
from django.db import models
# Create your models here.


class Blog(models.Model):
    title = models.CharField(max_length=200)
    created = models.DateTimeField(auto_now_add=True)
    description_1 = models.TextField('Description 1', blank=True, null=True)
    description_2 = models.TextField('Description 2', blank=True, null=True)
    blog_image = models.ImageField(blank=True, null=True)
    id = models.UUIDField(default=uuid.uuid4, unique=True,
                          primary_key=True, editable=False)

    def __str__(self):
        return self.title


class BlogComment(models.Model):
    name = models.CharField('Name', max_length=50)
    email = models.EmailField('Email')
    comment = models.TextField('Comment', blank=True, null=True)
    created = models.DateTimeField(auto_now_add=True)
    id = models.UUIDField(default=uuid.uuid4, unique=True,
                          primary_key=True, editable=False)
    blog = models.ForeignKey(Blog, on_delete=models.CASCADE)

    def __str__(self):
        return self.name
