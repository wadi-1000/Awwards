from django.contrib.auth import login, logout, authenticate
from django.shortcuts import redirect, render
from django.contrib import messages
from django.views.generic import CreateView
from .forms import ViewerSignUpForm, EmployeeSignUpForm
from django.contrib.auth.forms import AuthenticationForm,UserCreationForm
from .models import User

def register(request):
    form = UserCreationForm()
    return render(request, 'registration/register.html',{'form': form})


