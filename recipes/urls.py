from django.urls import path
from recipes import views
from django.contrib.auth.views import PasswordResetConfirmView, PasswordResetCompleteView,PasswordResetDoneView



app_name = 'recipes'
urlpatterns = [
    path('', views.home, name='home'),
    path('login/', views.user_login, name='login'),
    path('upload/', views.upload_recipe, name='upload'),
    path('register/', views.register, name='register'),
    path('logout/', views.user_logout, name='logout'),
    path('password_reset_form/', views.reset_password, name='password_reset_form'), 
    path('edit_profile/', views.user_edit_profile, name='edit_profile'), 
    path('search/', views.search, name='search'),
    path('recipe/<slug:recipe_slug>/', views.recipe_page, name='recipe_page'),
    path('category/<slug:category_slug>/', views.category_detail, name='category_detail'),
    path('like_recipe/', views.LikeRecipeView.as_view(), name='like_recipe'),
    path('goto/<slug:slug>/', views.goto_url, name='goto'),
    path('profile/', views.view_profile, name='view_profile'),
    path('upload_review/<int:recipeID>/', views.upload_review, name='upload_review'),
    path('recipes/add_to_favourites/<int:recipe_id>/', views.add_to_favourites, name='add_to_favourites'),
    path('recipes/<int:recipe_id>/reviews/', views.recipe_reviews, name='recipe_reviews'),
    path('most-viewed/', views.most_viewed_recipes, name='most_viewed_recipes'),
    path('most-liked/', views.most_liked_recipes, name='most_liked_recipes'),
]