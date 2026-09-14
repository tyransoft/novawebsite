from django.urls import path
from .views import *
from django.contrib.sitemaps.views import sitemap
from .sitemaps import StaticViewSitemap

sitemaps = {
    "static": StaticViewSitemap,
}

urlpatterns = [

    path('', home, name='home'),

    path('products/', products, name='products'),
    path('products/baby-diapers/',pampers,name='products_baby_diapers'),
    path('products/wipes/',wipes,name='products_wipes'),
    path('products/personal-care/',mothers,name='products_personal_care'),

    path('about/',about,name='about'),

    path('quality/',quality,name='quality'),
    path('why-us/',why_us,name='why_us'),
    path('our-story/',our_story,name='ourstory'),
    path('connect-us/',connect_us,name='connectus'),

    path("sitemap.xml", sitemap, {"sitemaps": sitemaps}, name="django_sitemap"),





]
