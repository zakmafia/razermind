from django.contrib import admin
from .models import Tag, Project, ProjectPhoto, UserProject
# Register your models here.

admin.site.register(Tag)
admin.site.register(Project)
admin.site.register(ProjectPhoto)
admin.site.register(UserProject)