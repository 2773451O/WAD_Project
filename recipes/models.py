from django.db import models
from django.contrib.auth.models import User
from django.template.defaultfilters import slugify

class UserProfile(models.Model):
    
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    picture = models.ImageField(default = 'photo_placeholder.png', upload_to='profile_images', blank=True)
    bio = models.TextField(blank=True)
    favourite_recipes = models.TextField(blank=True) 

    def __str__(self):
        return self.user.username

class Category(models.Model):
    NAME_MAX_LENGTH = 128
    id = models.BigAutoField(primary_key=True)
    name = models.CharField(max_length=NAME_MAX_LENGTH, unique=True)
    views = models.IntegerField(default=0)
    likes = models.IntegerField(default=0)
    slug = models.SlugField(unique=True, blank=True)

    def save(self, *args, **kwargs):
        self.slug = slugify(self.name)
        super(Category, self).save(*args, **kwargs)

    class Meta:
        verbose_name_plural = 'Categories'

    def __str__(self):
        return self.name

class Recipe(models.Model):
    id = models.BigAutoField(primary_key=True)
    title = models.CharField(max_length=255)
    description = models.TextField()
    categories = models.ManyToManyField(Category)
    ingredients = models.TextField()
    difficulty = models.TextField()
    author = models.ForeignKey(User, on_delete=models.CASCADE, null=True)
    directions = models.TextField()
    image = models.ImageField(upload_to='recipes/')
    slug = models.SlugField(unique=True)

    views = models.IntegerField(default=0)
    likes = models.IntegerField(default=0)

    def save(self, *args, **kwargs):
        self.slug = slugify(self.title)
        super(Recipe, self).save(*args, **kwargs)

    def __str__(self):
        return self.title
    

