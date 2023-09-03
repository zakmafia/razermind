from django.contrib import admin
from .models import Tag, Project, ProjectPhoto, UserProject, BannerImage
# Register your models here.


class TagAdmin(admin.ModelAdmin):
    prepopulated_fields = {'slug': ('name',)}
    list_display = ('name', )


admin.site.register(Tag, TagAdmin)
admin.site.register(Project)
admin.site.register(ProjectPhoto)
admin.site.register(UserProject)
admin.site.register(BannerImage)