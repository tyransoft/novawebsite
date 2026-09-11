from django.urls import path
from .views import *
from django.contrib.sitemaps.views import sitemap


urlpatterns = [

    path('', home, name='home'),

    path('products/', products, name='products'),
    path('products/baby-diapers/',pampers,name='pampers'),
    path('products/wipes/',wipes,name='wipes'),
    path('products/personal-care/',mothers,name='mothers'),

    path('about/',about,name='about'),

    path('quality/',quality,name='quality'),
    path('why-us/',why_us,name='why_us'),
    path('our-story/',our_story,name='ourstory'),
    path('connect-us/',connect_us,name='connectus'),







]
