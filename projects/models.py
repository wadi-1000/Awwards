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
    rating = (
        (1, '1'),
        (2, '2'),
        (3, '3'),
        (4, '4'),
        (5, '5'),
        (6, '6'),
        (7, '7'),
        (8, '8'),
        (9, '9'),
        (10, '10'),
    )

    design = models.IntegerField(choices=rating, default=0, blank=True)
    usability = models.IntegerField(choices=rating, blank=True)
    content = models.IntegerField(choices=rating, blank=True)
    score = models.FloatField(default=0, blank=True)
    design_average = models.FloatField(default=0, blank=True)
    usability_average = models.FloatField(default=0, blank=True)
    content_average = models.FloatField(default=0, blank=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=True, related_name='rater')
    project = models.ForeignKey(Project, on_delete=models.CASCADE, related_name='ratings', null=True)

    def save_rating(self):
        self.save()

    @classmethod
    def get_ratings(cls, id):
        ratings = Rating.objects.filter(post_id=id).all()
        return ratings

    def __str__(self):
        return f'{self.post} Rating'