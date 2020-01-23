from blog.sitemaps import ArticleSitemap, CategorySitemap, IndexSitemap
from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.contrib.sitemaps.views import sitemap
from django.urls import path, include

sitemaps = {
    'index': IndexSitemap,
    'categorys': CategorySitemap,
    'articles': ArticleSitemap,
}

urlpatterns = [
    path('admin/', admin.site.urls),
    path('sitemap.xml/', sitemap, {'sitemaps': sitemaps},  name='sitemap'),
    path('markdownx/', include('markdownx.urls')), # Markdownx 用
    path('', include('blog.urls')),
]

urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
