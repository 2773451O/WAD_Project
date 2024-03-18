from django.db import models
from django.contrib.auth.models import User

class UserProfile(models.Model):
    
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    picture = models.ImageField(default = 'photo_placeholder.png',upload_to='profile_images', blank=True)

    def __str__(self):
        return self.user.username
    
class UserProfile(models.Model):
    
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    picture = models.ImageField(upload_to='profile_images', blank=True)
    bio = models.TextField(blank=True)
    favourite_recipes = models.TextField(blank=True) 

    def __str__(self):
        return self.user.username


