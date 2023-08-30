from django.forms import ModelForm
from django import forms
from django.forms import ClearableFileInput
from .models import Project, ProjectPhoto


class ProjectForm(ModelForm):
    class Meta:
        model = Project
        fields = ['name', 'description', 'project_image', 'tags']
        widgets = {
            'tags': forms.CheckboxSelectMultiple(),
        }


class ProjectImageForm(forms.ModelForm):
    class Meta:
        model = ProjectPhoto
        fields = ['images']
        widgets = {
            'images': ClearableFileInput(),
        }
