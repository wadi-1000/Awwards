from django.contrib.auth import login, logout, authenticate
from django.shortcuts import redirect, render
from django.contrib import messages
from django.views.generic import CreateView
from .form import ViewerSignUpForm, EmployeeSignUpForm
from django.contrib.auth.forms import AuthenticationForm
from .models import 

def register(request):
    return render(request, 'registration/register.html')


class viewer_register(CreateView):
    model = User
    form_class = ViewerSignUpForm
    template_name = 'registration/viewer_register.html'

    def form_valid(self, form):
        user = form.save()
        login(self.request, user)
        return redirect('/')


class employee_register(CreateView):
    model = User
    form_class = EmployeeSignUpForm
    template_name = 'registration/employee_register.html'

    def form_valid(self, form):
        user = form.save()
        login(self.request, user)
        return redirect('/')
