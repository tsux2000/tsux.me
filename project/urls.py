"""
Project URL Configuration
"""

from blog import sitemaps
from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.contrib.sitemaps.views import sitemap
from django.urls import path, include
from django.views.generic import TemplateView

urlpatterns = [
    path('admin/', admin.site.urls),
    path('sitemap.xml/', sitemap, {
        'sitemaps': {
            'index': sitemaps.IndexSitemap,
            'categorys': sitemaps.CategorySitemap,
            'articles': sitemaps.ArticleSitemap,
        }
    },  name='sitemap'),
    path('robots.txt/', TemplateView.as_view(template_name="robots.txt", content_type='text/plain')),
    path('markdownx/', include('markdownx.urls')),
    path('', include('blog.urls')),
]

urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
