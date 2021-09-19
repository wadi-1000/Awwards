from django.db import models
from cloudinary.models import CloudinaryField
from django.contrib.auth.models import User
from users.models import Profile
# Create your models here.

class Project(models.Model):
    name = models.CharField(max_length = 30)
    screenshot = CloudinaryField('Project screenshot')
    description = models.TextField()
    link = models.URLField()
    profile = models.ForeignKey(Profile, on_delete=models.CASCADE)
    voters = models.IntegerField(default=0)
    post_date = models.DateTimeField(auto_now_add=True, null = True)
    average_design = models.FloatField(default=0,)
    average_usability = models.FloatField(default=0)
    average_content = models.FloatField(default=0)
    average_score = models.FloatField(default=0)

    def __str__(self):
        return self.name

    def save_project(self):
        self.save()

    def delete_project(self):
        self.delete()

    def voters_count(self):
        return self.voters.count()

    @classmethod
    def display_all_projects(cls):
        return cls.objects.all()

    @classmethod 
    def search_project(cls,name):
        return Project.objects.filter(name__icontains = name)

    @classmethod
    def get_user_projects(cls,profile):
        return cls.objects.filter(profile=profile)

    class Meta:
        ordering = ['-post_date']
    
class IntegerRangeField(models.IntegerField):
    def __init__(self, verbose_name=None, name=None, min_value=None, max_value=None, **kwargs):
        self.min_value, self.max_value = min_value, max_value
        models.IntegerField.__init__(self, verbose_name, name, **kwargs)
    def formfield(self, **kwargs):
        defaults = {'min_value': self.min_value, 'max_value':self.max_value}
        defaults.update(kwargs)
        return super(IntegerRangeField, self).formfield(**defaults)