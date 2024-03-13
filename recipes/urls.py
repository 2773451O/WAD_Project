from django.urls import path
from recipes import views
from django.contrib.auth.views import PasswordResetConfirmView, PasswordResetCompleteView,PasswordResetDoneView



app_name = 'recipes'
urlpatterns = [
    path('', views.home, name='home'),
    path('login/', views.user_login, name='login'),
    path('upload/', views.upload_review, name='upload'),
    path('register/', views.register, name='register'),
    path('logout/', views.user_logout, name='logout'),
    path('password_reset_form/', views.reset_password, name='password_reset_form'),  
]