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

class MultipleFileInput(forms.ClearableFileInput):
    allow_multiple_selected = True

class MultipleFileField(forms.FileField):
    def __init__(self, *args, **kwargs):
        kwargs.setdefault("widget", MultipleFileInput())
        super().__init__(*args, **kwargs)

    def clean(self, data, initial=None):
        single_file_clean = super().clean
        if isinstance(data, (list, tuple)):
            result = [single_file_clean(d, initial) for d in data]
        else:
            result = single_file_clean(data, initial)
        return result

class ProjectImageForm(forms.Form):
    images = MultipleFileField()


