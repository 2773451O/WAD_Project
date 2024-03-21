from django import forms
from django.contrib.auth.models import User 
from recipes.models import UserProfile, Recipe, Review

class UserForm(forms.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput())

    class Meta:
        model = User
        fields = ('username', 'first_name', 'last_name', 'email', 'password',)

class UserProfileForm(forms.ModelForm): 
    class Meta:
        model = UserProfile
        fields = ('picture', 'bio', 'favourite_recipes',)


class SearchForm(forms.ModelForm):
    query = forms.CharField(label='Search', max_length=100)

    class Meta:
        model = Recipe
        fields = ('query',)

class UploadForm(forms.ModelForm):
    #ingredients = forms.CharField(widget=forms.Textarea(attrs={'rows':3}))
    #description = forms.CharField(widget=forms.Textarea(attrs={'rows':3}))
    #directions = forms.CharField(widget=forms.Textarea(attrs={'rows':3}))

   # likes = forms.IntegerField(widget=forms.HiddenInput(), initial=0)
    image = forms.FileField(required = False)
   # views = forms.IntegerField(widget=forms.HiddenInput(), initial=0)
    #user = User(initial=0)
    class Meta:
        model = Recipe
        fields = ('title','ingredients','description','directions', 'image', 'categories','difficulty','author')
        exclude = ('likes', 'views', 'author')


class ReviewForm(forms.ModelForm):
    description = forms.CharField(widget=forms.Textarea(attrs={'rows':3}))
    reviewId = forms.CharField(widget=forms.HiddenInput())
    class Meta:
        model = Review
        fields = ('title','rating','description')