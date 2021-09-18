from django.contrib.auth.forms import UserCreationForm
from django import forms
from django.db import transaction
from .models import User, Viewer, Owner


class ViewerSignUpForm(UserCreationForm):
    name = forms.CharField(required=True)
    email = forms.EmailField(required=True)
    phone_number = forms.CharField(required=False)
    location = forms.CharField(required=True)

    class Meta(UserCreationForm.Meta):
        model = User

    @transaction.atomic
    def save(self):
        user = super().save(commit=False)
        user.is_viewer = True
        user.name = self.cleaned_data.get('name')
        user.email = self.cleaned_data.get('email')
        user.save()
        viewer = Viewer.objects.create(user=user)
        viewer.phone_number = self.cleaned_data.get('phone_number')
        viewer.location = self.cleaned_data.get('location')
        viewer.save()
        return user


# class OwnerSignUpForm(UserCreationForm):
#     name = forms.CharField(required=True)
#     email = forms.EmailField(required=True)
#     phone_number = forms.CharField(required=False)
#     designation = forms.CharField(required=True)

#     class Meta(UserCreationForm.Meta):
#         model = User

#     @transaction.atomic
#     def save(self):
#         user = super().save(commit=False)
#         user.is_project_owner = True
#         user.is_staff = True
#         user.first_name = self.cleaned_data.get('name')
#         user.email = self.cleaned_data.get('email')
#         user.save()
#         owner = Owner.objects.create(user=user)
#         owner.phone_number = self.cleaned_data.get('phone_number')
#         owner.designation = self.cleaned_data.get('designation')
#         owner.save()
#         return user