import os
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'Wad_Project.settings')

import django
django.setup()
from recipes.models import Recipe

def populate():
    recipes = [{'name':'Brownies', 'recipe':'add xyz cook long time yum'}, {'name':'Pizza', 'recipe':'add xyz cook long time yum'}, {'name':'Bread', 'recipe':'add xyz cook long time yum'}]

    for i in recipes:
        add_recipe(i['name'], i['recipe'])

def add_recipe(name,recipe):
    rec = Recipe.objects.get_or_create(name = name, recipe = recipe)[0]
    rec.save()
    return rec

if __name__ == '__main__':
    print('Starting population script...')
    populate()