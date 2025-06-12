from django import forms
from . import models

class ProjectCreateForm(forms.ModelForm):
    class Meta:
        model = models.Project
        fields = ['Category','title','description']
        widgets = {
            'Category': forms.Select(),
            'title': forms.TextInput(),
            'description' : forms.Textarea()
        }
