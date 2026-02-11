from django.urls import path
from django.conf import settings
from django.conf.urls.static import static
from mostafaraihan import views

urlpatterns = [
    path('', views.index, name='index'),
    path('post/<int:pk>/', views.techpost_detail, name='techpost_detail'),
    path('post/', views.post, name='post'),
    path('contact/', views.contact, name='contact'), 
    path('sitemap.xml/', views.sitemap, name='sitemap'),
    path('robots.txt/', views.robots, name='robots'),
]


if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)