from django.db import models
from cloudinary.models import CloudinaryField
from django.contrib.auth.models import User
from users.models import Profile
from django.urls import reverse
from django.core.validators import MaxValueValidator, MinValueValidator

# Create your models here.

class Project(models.Model):
    profile=models.ForeignKey(User, on_delete=models.CASCADE)
    title=models.CharField(max_length=500)
    image=CloudinaryField('image')
    description=models.TextField()
    link=models.CharField(max_length=1000)
    design_rate=models.IntegerField(default=0,
    validators=[
        MaxValueValidator(10),
        MinValueValidator(0)
    ])
    usability_rate=models.IntegerField(default=0,
    validators=[
        MaxValueValidator(10),
        MinValueValidator(0)
    ])
    content_rate=models.IntegerField(default=0,
    validators=[
        MaxValueValidator(10),
        MinValueValidator(0)
    ])
    average_review=models.IntegerField(default=0)


    def __str__(self):
        return self.title

    def save_project(self):
        self.save()

    def delete_project(self):
        self.delete()

    def search_by_title(search_term):
        projects=Project.objects.filter(title__icontains=search_term)
        return projects

class Rating(models.Model):
    design=models.ForeignKey(Project, related_name="design_rated", on_delete=models.CASCADE)
    design_rate=models.IntegerField()
    usability=models.ForeignKey(Project, related_name="usability_rated", on_delete=models.CASCADE)
    usability_rate=models.IntegerField()
    content=models.ForeignKey(Project, related_name="content_rated", on_delete=models.CASCADE)
    content_rate=models.IntegerField()

    def __str__(self):
        return self.design_rate