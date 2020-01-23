from blog.models import Article
from django.contrib.sitemaps import Sitemap
from django.shortcuts import resolve_url


class ArticleSitemap(Sitemap):
    changefreq = "never"
    priority = 0.5

    def items(self):
        return Article.objects.filter(del_flg=False)

    def location(self, obj):
        return resolve_url('article', pk=obj.slug)

    def lastmod(self, obj):
        return obj.create_date


class IndexSitemap(Sitemap):
    changefreq = "never"
    priority = 0.5

    def items(self):
        return ['index']

    def location(self, obj):
        return resolve_url(obj)

    def lastmod(self, obj):
        return obj.create_date
