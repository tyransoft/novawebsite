from django.contrib.sitemaps import Sitemap
from django.urls import reverse


class StaticViewSitemap(Sitemap):
    changefreq = "monthly"
    priority = 0.8

    def items(self):
        return [
            "home",
            "products",
            "products_baby_diapers",
            "products_wipes",
            "products_personal_care",
            "about",
            "quality",
            "why_us",
            "ourstory",
            "connectus",
        ]

    def location(self, item):
        return reverse(item)