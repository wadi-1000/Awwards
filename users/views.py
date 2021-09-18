from django.shortcuts import render, redirect
from django.contrib import messages
from .forms import UserRegisterForm,  ProfileUpdateForm
from .models import Profile



def register(request):
    if request.method == 'POST':
        form = UserRegisterForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            return redirect('login')

    else:
        form = UserRegisterForm()
    return render(request, 'users/registration.html', {"form":form})


def profile(request):
    
    profile = Profile.objects.get_or_create(user=request.user)
    if request.method =='POST':
        profile_update_form = ProfileUpdateForm(request.POST or None, request.FILES, instance=request.user.profile)
        if profile_update_form.is_valid():
            profile_update_form.save()
            return redirect('profile')
    else:
        profile_update_form = ProfileUpdateForm()

    context = {
        'profile_update_form': profile_update_form,
        
    }
    return render(request, 'users/profile.html', context)

