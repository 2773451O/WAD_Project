import os
import django
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'Wad_Project.settings')

django.setup()
from recipes.models import Recipe, Category, User

def populate():
    recipes_data = [
        {
            'title': 'Greggs sausage rolls',
            'category_name': 'Pastys',
            'ingredients': 'Pastry\nHopefully pig',
            'difficulty': 'Hard',
            'username': 'Chico Bear',
            'directions': 'Put in microware till lukewarm',
            'views': 100334324343244343,
            'likes': 334384384903847
        },
    ]

    for recipe_data in recipes_data:
        category_name = recipe_data.pop('category_name')
        category, _ = Category.objects.get_or_create(name=category_name)

        # Get or create the author (assuming you have a User model)
        author_name = recipe_data.pop('username')
        author, _ = User.objects.get_or_create(username=author_name)

        # Create the recipe object
        recipe = Recipe.objects.create(author=author, **recipe_data)
        recipe.categories.set([category])  # Set the categories for the recipe


if __name__ == '__main__':
    print('Starting WAD population script...')
    populate()