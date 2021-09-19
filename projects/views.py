from django.shortcuts import render, redirect
from django.http import HttpResponse
from .forms import  UploadNewProject
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from django.views.generic.edit import CreateView
from .models import  Project
from django.contrib.auth.decorators import login_required
# Create your views here.
def home(request):
   
   
    return render(request, 'home.html')


@login_required
def viewProject(request, pk):
    project=Project.objects.filter(id=pk)
    current_user=request.user

    return render(request, 'projects/project.html', {"project":project})

@login_required
def uploadProject(request):
    form=UploadNewProject()
    current_user=request.user

    if request.method =="POST":
        form=UploadNewProject(request.POST, request.FILES)
        if form.is_valid():
            project=form.save(commit=False)
            project.profile=current_user
            project.save()

        return redirect('home')

    else:
        form=UploadNewProject()

    return render(request, 'uploadproject.html', {"form":form})
