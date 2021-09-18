from django.contrib import admin
from .models import User, Viewer, Employee

admin.site.register(User)
admin.site.register(Viewer)
admin.site.register(Employee)