from .models import Project, Profile
from django.forms import ModelForm
from django import forms


class AddProjectForm(ModelForm):
    class Meta:
        model = Project
        exclude = ['profile', 'post_date', 'voters', 'design_score','usability_score','content_score','average_design','average_usability','average_content','average_score']
