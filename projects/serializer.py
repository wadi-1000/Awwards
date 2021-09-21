from rest_framework import serializers
from users.models import Profile
from .models import Project

class ProfileSerializer(serializers.ModelSerializer):
    class Meta:
        model = Profile
        fields = ('user','bio','image')

class ProjectSerializer(serializers.ModelSerializer):
    class Meta:
        model = Project
        fields = ('profile','title','image','description','link')

        