from django.db import models
from django.contrib.auth.models import AbstractUser


class User(AbstractUser):
    is_employee = models.BooleanField(default=False)
    is_viewer = models.BooleanField(default=False)
    name = models.CharField(max_length=100)
    email = models.EmailField(max_length=60)


class Viewer(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, primary_key=True)
    phone_number = models.CharField(max_length=20)
    location = models.CharField(max_length=20)


# class Employee(models.Model):
#     user = models.OneToOneField(User, on_delete=models.CASCADE, primary_key=True)
#     phone_number = models.CharField(max_length=20)
#     designation = models.CharField(max_length=20)

