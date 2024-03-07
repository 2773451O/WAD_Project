from django import forms
from django.contrib.auth.models import User 
from recipes.models import UserProfile, Recipe

class UserForm(forms.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput())

    class Meta:
        model = User
        fields = ('username', 'first_name', 'last_name', 'email', 'password',)

class UserProfileForm(forms.ModelForm): 
     class Meta:
        model = UserProfile
        fields = ('picture',)

class UploadForm(forms.ModelForm):
    name = forms.CharField(max_length = 256, help_text = "Please enter the name of the recipe")
    recipe = forms.CharField(max_length = 2000000, help_text = "Please enter your recipe here")