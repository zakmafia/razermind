from django.forms import ModelForm
from django import forms
from .models import Project

class ProjectForm(ModelForm):
    class Meta:
        model = Project
        fields = ['name', 'description', 'project_image', 'tags']
        widgets = {
                'tags': forms.CheckboxSelectMultiple(),
            }
        

        