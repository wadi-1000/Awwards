from django.urls import path

from django.contrib.auth import views as auth_views

from . import views

urlpatterns = [
    # login/signup &logout
    path('home/', views.home, name='home'),  
   
]