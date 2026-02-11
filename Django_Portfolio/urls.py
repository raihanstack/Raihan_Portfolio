from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
from mostafaraihan.admin import custom_admin_site  # <-- Custom admin import

urlpatterns = [
    path('admin/', custom_admin_site.urls),  # Custom admin route
    path('', include('mostafaraihan.urls')),  # Your app URLs
]

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
