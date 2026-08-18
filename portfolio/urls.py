"""
URL configuration for portfolio project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/6.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path , include
from django.conf import settings
from django.conf.urls.static import static
from django.contrib.sitemaps.views import sitemap
from portfolio.sitemaps import StaticViewSitemap
from django.views.generic import TemplateView

urlpatterns = [
    path('admin/', admin.site.urls),
    path('',include ('home.urls')),
    path('about/', include('about.urls')),
    path('skills/', include('skills.urls')),
    path('projects/', include('projects.urls')),
    path('services/' , include('services.urls')),
    path('contact/', include('contact.urls'),),
    path('blog/', include('blog.urls')),
    path('resume/',include('resume.urls')),
    path('accounts/', include('accounts.urls')),
    path('dashboard/', include('dashboard.urls')),
    path('sitemap.xml',sitemap,{'sitemaps': {'static': StaticViewSitemap}},name='django-sitemap',),
    path(
        'robots.txt',
        TemplateView.as_view(
            template_name='robots.txt',
            content_type='text/plain'
        ),
        name='robots.txt',
    ),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
