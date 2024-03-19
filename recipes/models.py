from django.db import models
from django.contrib.auth.models import User

class UserProfile(models.Model):
    
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    picture = models.ImageField(default = 'photo_placeholder.png',upload_to='profile_images', blank=True)
    bio = models.TextField(blank=True)
    favourite_recipes = models.TextField(blank=True) 

    def __str__(self):
        return self.user.username
    

class Category(models.Model):
    id = models.BigAutoField(primary_key=True)
    name = models.CharField(max_length=200)

    def __str__(self):
        return self.name
    
class Recipe(models.Model):
    id = models.BigAutoField(primary_key=True)
    title = models.CharField(max_length=200)
    category = models.ForeignKey(Category, on_delete=models.SET_NULL, null=True, blank=True)
    ingredients = models.TextField()
    difficulty = models.TextField()
    author = models.ForeignKey(User, on_delete=models.CASCADE, null=True)
    directions = models.TextField()

    views = models.IntegerField(default=0)
    likes = models.IntegerField(default=0)

    def __str__(self):
        return self.title
