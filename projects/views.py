from django.shortcuts import render, redirect
from django.http import HttpResponse,JsonResponse,HttpResponseRedirect
from .forms import  UploadNewProject,RatingsForm
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from django.views.generic.edit import CreateView
from .models import  Project,Rating
from django.contrib.auth.decorators import login_required
from rest_framework.response import Response
from rest_framework.views import APIView
from users.models import  Profile
from .serializer import ProjectSerializer,ProfileSerializer
from rest_framework import status
from .permissions import IsAdminOrReadOnly
# Create your views here.
def home(request):
    projects=Project.objects.all()
    context = {
       
        'projects':projects
    }
    return render(request, "home.html", context)





def viewProject(request, pk):
    project=Project.objects.filter(id=pk)
    current_user=request.user


    return render(request, 'project.html', {"project":project})

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
@login_required
def searchProject(request):
    
    if 'project' in request.GET and request.GET['project']:
        search_term=request.GET.get('project')
        searched_projects=Project.search_by_title(search_term)
        message=f"{search_term}"

        return render(request, "search.html", {"projects":searched_projects, "message":message})
    else:
        message="You have not searched for any project"
        return render(request, "search.html")
@login_required
def rate(request,id):
    project=Project.objects.get(pk=id)
    current_user=request.user
    ratings = Rating.objects.filter(user=request.user, project=project)
    rating_status = None
    if ratings is None:
        rating_status = False
    else:
        rating_status = True
    if request.method == 'POST':
        form = RatingsForm(request.POST)
        if form.is_valid():
            rate = form.save(commit=False)
            rate.user = request.user
            rate.project = project
            rate.save()
            post_ratings = Rating.objects.filter(project=project)

            design_ratings = [d.design for d in post_ratings]
            design_average = sum(design_ratings) / len(design_ratings)

            usability_ratings = [us.usability for us in post_ratings]
            usability_average = sum(usability_ratings) / len(usability_ratings)

            content_ratings = [content.content for content in post_ratings]
            content_average = sum(content_ratings) / len(content_ratings)

            score = (design_average + usability_average + content_average) / 3
            print(score)
            rate.design_average = round(design_average, 2)
            rate.usability_average = round(usability_average, 2)
            rate.content_average = round(content_average, 2)
            rate.score = round(score, 2)
            rate.save()
            return redirect('home')
    else:
        form = RatingsForm()
    params = {
        'project': project,
        'form': form,
        'rating_status': rating_status

    }
    return render(request, 'rateprojects.html', params)


class ProjectList(APIView):
    permission_classes = (IsAdminOrReadOnly,)
    def get(self, request, format=None):
        all_projects = Project.objects.all()
        serializers = ProjectSerializer(all_projects, many = True)
        return Response(serializers.data)

    def post(self, request, format=None):
        serializers = ProjectSerializer(data=request.data)
        if serializers.is_valid():
            serializers.save()
            return Response(serializers.data, status=status.HTTP_201_CREATED)
        return Response(serializers.errors, status=status.HTTP_400_BAD_REQUEST)


class ProfileList(APIView):
    permission_classes = (IsAdminOrReadOnly,)
    def get(self, request, format=None):
        all_profiles = Profile.objects.all()
        serializers = ProfileSerializer(all_profiles, many = True)
        return Response(serializers.data)


    def post(self, request, format=None):
            serializers = ProfileSerializer(data=request.data)
            if serializers.is_valid():
                serializers.save()
                return Response(serializers.data, status=status.HTTP_201_CREATED)
            return Response(serializers.errors, status=status.HTTP_400_BAD_REQUEST)