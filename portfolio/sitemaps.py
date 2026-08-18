from django.contrib.sitemaps import Sitemap
from django.urls import reverse


class StaticViewSitemap(Sitemap):
    priority = 0.8
    changefreq = "weekly"

    def items(self):
        return [
            "home",
            "about",
            "skills",
            "projects",
            "services",
            "contact",
            "blog",
            "resume",
        ]

    def location(self, item):
        return reverse(item)