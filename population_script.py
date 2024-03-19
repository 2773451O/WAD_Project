import os
import django
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'Wad_Project.settings')

django.setup()
from recipes.models import Recipe, Category, User

def populate():
    recipes_data = [
        {
            'title': 'Spaghetti Bolognese',
            'category_name': 'Italian',
            'ingredients': 'Spaghetti\nMince meat\nTomatoes',
            'difficulty': 'Easy',
            'username': 'hannah',
            'directions': 'First, boil the pasta\nSecond, fry off some chopped onions\nThird, add the meat and cook through',
            'views': 100,
            'likes': 37
        },
    ]

    for recipe_data in recipes_data:
        category_name = recipe_data.pop('category_name')
        category, _ = Category.objects.get_or_create(name=category_name)

        # Get or create the author (assuming you have a User model)
        author_name = recipe_data.pop('username')
        author, _ = User.objects.get_or_create(username=author_name)

        # Create the recipe object
        recipe = Recipe.objects.create(category=category, author=author, **recipe_data)



if __name__ == '__main__':
    print('Starting WAD population script...')
    populate()

