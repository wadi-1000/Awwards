from .models import Project,Rating
from django.forms import ModelForm
from django import forms
from users.models import Profile


class UploadNewProject(forms.ModelForm):
    class Meta:
        model=Project
        exclude=['design_rating', 'usability_rating', 'content_rating', 'average_review', 'profile']
        fields=['title', 'image', 'description', 'link']

class RatingsForm(forms.ModelForm):
    class Meta:
        model = Rating
        fields = ['design', 'usability', 'content']