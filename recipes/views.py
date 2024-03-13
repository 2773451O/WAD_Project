from django.shortcuts import render
from django.http import HttpResponse
from django.shortcuts import redirect
from django.urls import reverse
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from datetime import datetime
from recipes.forms import UserForm, UserProfileForm
from django.contrib.auth import authenticate
from django.contrib.auth.models import User
from django.contrib.auth.forms import PasswordResetForm
from recipes.models import UserProfile



def home(request):
    
    context_dict = {}
    context_dict['Page'] = 'Home'
    response = render(request, 'recipes/home.html', context=context_dict)
    return response
    
def user_login(request):
    context_dict = {}
    context_dict['Page'] = 'Log in'

    if request.method == 'POST':
        username = None  # Initialize username variable

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
                return HttpResponse("Your Culinary Carnival account is disabled.")
        else:
            return HttpResponse("Invalid login details supplied.")
    else:
        return render(request, 'recipes/login.html', context=context_dict)
 
def upload_review(request):
    
    context_dict = {}
    context_dict['Page'] = 'Upload Review'
    return render(request, 'recipes/upload.html', context=context_dict)

def register(request):

    registered = False
    
    if request.method == 'POST':

        user_form = UserForm(request.POST)
        profile_form = UserProfileForm(request.POST)
       
        if user_form.is_valid() and profile_form.is_valid(): 
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
                return HttpResponse("Username or Email already exists please choose another.")
    else:

        user_form = UserForm()
        profile_form = UserProfileForm()
    
    return render(request, 'recipes/register.html',
                  context = {'user_form': user_form,
                             'profile_form': profile_form,
                             'registered': registered,
                             'Page' : 'Register'})

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