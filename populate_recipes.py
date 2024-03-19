import os
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'Wad_Project.settings')

import django
django.setup()
from recipes.models import Recipe

def populate():
    recipes = [{'name':'Brownies', 'ingredients':'flour egg idk', 'instructions':'add xyz cook long time yum', 'likes':0, 'picture':'cookies.jpg', 'views':24}, {'name':'Pizza', 'ingredients':'flour egg idk', 'instructions':'add xyz cook long time yum', 'likes':20, 'picture':'cookies.jpg', 'views':56}, {'name':'Bread', 'ingredients':'flour egg idk', 'instructions':'add xyz cook long time yum', 'likes':7, 'picture':'cookies.jpg', 'views':16}]

    for i in recipes:
        add_recipe(i['name'], i['ingredients'], i['instructions'], i['likes'], i['picture'], i['views'])

def add_recipe(name,ingredients,instructions, likes, picture, views):
    rec = Recipe.objects.get_or_create(name = name, ingredients = ingredients, instructions = instructions, likes=likes, picture=picture, views=views)[0]
    rec.save()
    return rec

if __name__ == '__main__':
    print('Starting population script...')
    populate()