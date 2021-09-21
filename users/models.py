from django.db import models
from django.contrib.auth.models import User
from cloudinary.models import CloudinaryField
class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, null=True)
    image = CloudinaryField(default='default.jpeg')
    bio = models.TextField( default="Please Update Bio")
    location=models.CharField(max_length = 50)
    number = models.IntegerField(default =0)
    email = models.EmailField(default = "Enter your valid email address")

    def __str__(self):
        return '{} {}'.format(self.image.url, self.bio)


    def save_profile(self):
        self.save()