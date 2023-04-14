from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('accounts.urls')),
    path('', include('stack_eng.urls')),
    path('', include('allauth.urls'), name = 'social'),
] + static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)
