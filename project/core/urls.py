from django.urls import path
from .views import *
from django.contrib.sitemaps.views import sitemap


urlpatterns = [

    path('', home, name='home'),
  
]
