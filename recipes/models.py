from django.db import models
from django.contrib.auth.models import User

class UserProfile(models.Model):
    
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    picture = models.ImageField(upload_to='profile_images', blank=True)

    def __str__(self):
        return self.user.username

class Recipe(models.Model):
    name = models.CharField(max_length = 256, unique = True)
    recipe = models.CharField(max_length = 2000000)

    class Meta:
        verbose_name_plural = 'Recipes'

    def __str__(self):
        return self.name