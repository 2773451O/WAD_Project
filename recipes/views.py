from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse
from django.shortcuts import redirect
from django.urls import reverse
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from datetime import datetime
from recipes.forms import ReviewForm, UserForm, UserProfileForm, SearchForm, UploadForm
from django.contrib.auth import authenticate
from django.contrib.auth.models import User
from django.contrib.auth.forms import PasswordResetForm
from recipes.models import UserProfile, Recipe, Category, Review
from django.db.models import Q
from django.views import View
from django.utils.decorators import method_decorator




def home(request):
    recipe = Recipe.objects.all()
    categories = Category.objects.all()  
    context_dict = {'Page': 'Home', 'categories': categories, 'recipes': recipe}
    response = render(request, 'recipes/home.html', context=context_dict)
    return response

    
def user_login(request):
    context_dict = {}
    context_dict['Page'] = 'Log in'

    if request.method == 'POST':
        username = None  

        username_or_email = request.POST.get('username')
        password = request.POST.get('password')

        if '@' in username_or_email:
            try:
                user = User.objects.get(email=username_or_email)
                username = user.username
            except User.DoesNotExist:
                user = None
        else:
            username = username_or_email

        user = authenticate(username=username, password=password)

        if user:
            if user.is_active:
                login(request, user)
                return redirect(reverse('recipes:home'))
            else:
               context_dict['error'] = 'Your culinary carnival account is disabled'
            return render(request, 'recipes/login.html', context=context_dict)
        else:
            context_dict['error'] = 'Invalid login details supplied'
            return render(request, 'recipes/login.html', context=context_dict)
    else:
        return render(request, 'recipes/login.html', context=context_dict)
 

def upload_review(request, recipeID):
    if request.method == 'POST':
        form = ReviewForm(request.POST)
        if form.is_valid():
            review = form.save(commit=False)
            review.author = request.user  
            recipe_instance = get_object_or_404(Recipe, id=recipeID)
            review.recipe = recipe_instance 
            review.save()

            return redirect('recipes:home')  
        else:
            print(form.errors)
    else:
        form = ReviewForm()
    
    return render(request, 'recipes/upload_review.html', {'form': form, 'recipeID': recipeID})

def register(request):
    registered = False

    if request.method == 'POST':
        user_form = UserForm(request.POST)
        profile_form = UserProfileForm(request.POST)
       
        if user_form.is_valid() and profile_form.is_valid():
            email = user_form.cleaned_data['email']
            if User.objects.filter(email=email).exists():
                return render(request, 'recipes/register.html',
                              context={'user_form': user_form,
                                       'profile_form': profile_form,
                                       'registered': registered,
                                       'Page': 'Register',
                                       'error': "Email already exists. Please use a different email."})

            user = user_form.save()
            user.set_password(user.password)
            user.save()
            
            profile = profile_form.save(commit=False)
            profile.user = user

            if 'picture' in request.FILES:
                profile.picture = request.FILES['picture']
                
            profile.save()

            user = authenticate(username=user_form.cleaned_data['username'],
                                password=user_form.cleaned_data['password'])
            login(request, user)
            registered = True
            return redirect('recipes:home')

        else:
            return render(request, 'recipes/register.html',
                          context={'user_form': user_form,
                                   'profile_form': profile_form,
                                   'registered': registered,
                                   'Page': 'Register',
                                   'error': "Invalid details, please try again"})
    else:
        user_form = UserForm()
        profile_form = UserProfileForm()
    
    return render(request, 'recipes/register.html',
                  context={'user_form': user_form,
                           'profile_form': profile_form,
                           'registered': registered,
                           'Page': 'Register'})

@login_required
def user_logout(request):
    logout(request)
   
    return redirect(reverse('recipes:home'))



def reset_password(request):
    if request.method == "POST":
        form = PasswordResetForm(request.POST)
        if form.is_valid():
            form.save(  
                request=request,
                use_https=request.is_secure(),
                email_template_name='registration/password_reset_email.html',
                subject_template_name='registration/password_reset_subject.txt',
                from_email=None,
                html_email_template_name=None,
                extra_email_context=None,
            )  
            return render(request, 'recipes/password_reset_done.html')

    else:
        form = PasswordResetForm()
    return render(request, 'recipes/password_reset_form.html', {'form': form})

@login_required
def user_edit_profile(request):
    user_profile, created = UserProfile.objects.get_or_create(user=request.user)

    if request.method == 'POST':
        form = UserProfileForm(request.POST, request.FILES, instance=user_profile)
        if form.is_valid():
            form.save()
            return redirect('recipes:view_profile')  
    else:
        form = UserProfileForm(instance=user_profile)

    context_dict = {
        'form': form,
        'Page': 'Edit Profile',
    }
    return render(request, 'recipes/edit_profile.html', context_dict)



def search(request):
    if request.method == 'GET':
        form = SearchForm(request.GET)
        if form.is_valid():
            query = form.cleaned_data['query']
            recipe_results = Recipe.objects.filter(
                Q(title__icontains=query) |
                Q(ingredients__icontains=query) |
                Q(directions__icontains=query) |
                Q(categories__name__icontains=query) |
                Q(author__username__icontains=query)
                
            ).distinct()  # removes duplicates
            return render(request, 'recipes/search.html', context={'recipe_results': recipe_results, 'query': query})
        else:
            form = SearchForm()
        return render(request, 'recipes/search.html', context={'form': form,'Page' : 'Search'})
    

def category_detail(request, category_slug):
    context_dict = {}
    try:
        categories = Category.objects.all()
        category = Category.objects.get(slug=category_slug)
        recipes = Recipe.objects.filter(categories=category)
        context_dict['Page'] = category.name
        context_dict['category']=category
        context_dict['recipes']= recipes
        context_dict['categories'] = categories

    except Category.DoesNotExist:
        context_dict['category'] =None
        context_dict['recipes'] = None
        context_dict['categories'] = Category.objects.all()

    return render(request, 'recipes/category_detail.html', context=context_dict)

def recipe_page(request, recipe_slug):
    context_dict = {}
    categories = Category.objects.all()
    recipe = get_object_or_404(Recipe, slug=recipe_slug)
    context_dict['Page']= recipe.title
    context_dict['recipe'] = recipe
    context_dict['categories'] = categories
 
    return render(request, 'recipes/recipe_page.html', context=context_dict)

@login_required
def upload_recipe(request):
    categories = Category.objects.all()
    if request.method == 'POST':
        form = UploadForm(request.POST, request.FILES)
        if form.is_valid():
            recipe = form.save(commit=False)
            recipe.author = request.user  
            recipe.save()
            form.save_m2m()  
            return redirect(reverse('recipes:home'))
        else:
            print(form.errors)
    else:
        form = UploadForm()

    return render(request, 'recipes/upload.html', {'upload_form': form, 'categories': categories})

def goto_url(request, slug):
    recipe = get_object_or_404(Recipe, slug=slug)
    recipe.views += 1
    recipe.save()
    return redirect('recipes:recipe_page', recipe_slug=slug)

class LikeRecipeView(View):
    @method_decorator(login_required)
    def get(self, request):
        recipe_id = request.GET['recipe_id']
        try:
            recipe = Recipe.objects.get(id=int(recipe_id))
            print (recipe)
        except Recipe.DoesNotExist:
            print("doesnt exist")
            return HttpResponse(-1)
        except ValueError:
            return HttpResponse(-1)
        recipe.likes = recipe.likes + 1
        recipe.save()
        return HttpResponse(recipe.likes)
    
def view_profile(request):
    user_profile = get_object_or_404(UserProfile, user=request.user)

    context = {
        'user_profile': user_profile,
        'Page': 'View Profile',
    }
    return render(request, 'recipes/view_profile.html', context)

@login_required
def add_to_favourites(request, recipe_id):
    recipe = get_object_or_404(Recipe, pk=recipe_id)
    user_profile = UserProfile.objects.get_or_create(user=request.user)[0]  

    user_profile.favourite_recipes.add(recipe)
    user_profile.save()

    return redirect('recipes:recipe_page', recipe_slug=recipe.slug)


def recipe_reviews(request, recipe_id):
    recipe = get_object_or_404(Recipe, id=recipe_id)
    reviews = Review.objects.filter(recipe=recipe)
    context = {'recipe': recipe, 'reviews': reviews}
    return render(request, 'recipes/recipe_reviews.html', context)

def most_viewed_recipes(request):
    recipes = Recipe.objects.order_by('-views')[:5]  
    context = {'recipes': recipes}
    return render(request, 'recipes/most_viewed_recipes.html', context)

def most_liked_recipes(request):
    recipes = Recipe.objects.order_by('-likes')[:5]  
    context = {'recipes': recipes}
    return render(request, 'recipes/most_liked_recipes.html', context)

