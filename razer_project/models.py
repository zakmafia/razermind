import uuid
from django.db import models
# Create your models here.

class Tag(models.Model):
    name = models.CharField(max_length=200)
    created = models.DateTimeField(auto_now_add=True)
    id = models.UUIDField(default=uuid.uuid4, unique=True, primary_key=True, editable=False)

    def __str__(self):
        return self.name

class Project(models.Model):
    name = models.CharField('Name', max_length=50)
    tags = models.ManyToManyField(Tag, blank=True)
    id = models.UUIDField(default=uuid.uuid4, unique=True, primary_key=True, editable=False)
    description = models.TextField('Description', blank=True, null=True)
    project_image = models.ImageField(null=False, blank=False)

    def __str__(self):
        return self.name
    
class ProjectPhoto(models.Model):
    project = models.ForeignKey(Project, on_delete=models.SET_NULL, null=True, blank=True)
    images = models.ImageField(blank=True, null=True)
    id = models.UUIDField(default=uuid.uuid4, unique=True, primary_key=True, editable=False)