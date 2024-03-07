from django.urls import path
from recipes import views

app_name = 'recipes'
urlpatterns = [
    path('', views.home, name='home'),
    path('login/', views.user_login, name='login'),
    path('upload/', views.upload_review, name='upload'),
    path('register/', views.register, name='register'),
    path('logout/', views.user_logout, name='logout'),
]