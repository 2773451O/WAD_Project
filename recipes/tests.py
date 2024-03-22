from django.urls import reverse
from django.test import TestCase
from .models import Recipe, Category
from django.contrib.auth.models import User
from .forms import UserForm
from django.urls import resolve
from .views import home

class RecipeModelTest(TestCase):
    def test_recipe_creation(self):
        user = User.objects.create_user('testuser', 'test@example.com', 'testpassword')
        category = Category.objects.create(name="Dessert")
        recipe = Recipe.objects.create(
            title="Chocolate Cake",
            description="Delicious chocolate cake...",
            author=user
        )
        recipe.categories.add(category)

        self.assertEqual(recipe.title, "Chocolate Cake")
        self.assertTrue(recipe.categories.filter(name="Dessert").exists())
        self.assertEqual(str(recipe), recipe.title)  # Assuming you have __str__ method returning titl

class HomePageTest(TestCase):
    def test_home_page_status_code(self):
        response = self.client.get(reverse('recipes:home'))
        self.assertEqual(response.status_code, 200)

    def test_home_page_uses_correct_template(self):
        response = self.client.get(reverse('recipes:home'))
        self.assertTemplateUsed(response, 'recipes/home.html')

class UserFormTest(TestCase):
    def test_user_form_valid(self):
        form_data = {'username': 'newuser', 'email': 'user@example.com', 'password': 'password123'}
        form = UserForm(data=form_data)
        self.assertTrue(form.is_valid())

    def test_user_form_invalid(self):
        form_data = {}  # Empty data
        form = UserForm(data=form_data)
        self.assertFalse(form.is_valid())


class URLResolutionTest(TestCase):
    def test_home_url_resolves(self):
        resolver = resolve('/')
        self.assertEqual(resolver.func, home)