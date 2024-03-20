from django.contrib import admin
from django.urls import path
from django.urls import include
from recipes import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('', views.home, name='home'),
    path('recipes/', include('recipes.urls')),
    path('admin/', admin.site.urls),
    path('accounts/', include('django.contrib.auth.urls')),
    
]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
