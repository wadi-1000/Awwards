from django.urls import path
from rest_framework.authtoken.views import obtain_auth_token
from django.contrib.auth import views as auth_views

from . import views

urlpatterns = [
    # login/signup &logout
    path('home/', views.home, name='home'),  
    path('viewproject/<int:pk>/', views.viewProject, name="viewproject"),
    path('uploadproject/', views.uploadProject, name="uploadproject"),
    path('searchprojects/', views.searchProject, name="search_results"),
    path('rate/<int:id>/',views.rate, name = "rate"),
    path('api/projects/', views.ProjectList.as_view()),
    path('api/profile/',views.ProfileList.as_view()),
    path('api-token-auth/',obtain_auth_token),

]