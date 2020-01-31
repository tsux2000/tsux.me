
from blog import models
from django.contrib.sitemaps import Sitemap
from django.shortcuts import resolve_url


class ArticleSitemap(Sitemap):
    changefreq = "never"
    priority = 0.5

    def items(self):
        return models.Article.objects.filter(del_flg=False)

    def location(self, obj):
        return resolve_url('article', article_slug=obj.slug)

    def lastmod(self, obj):
        return obj.create_date

class CategorySitemap(Sitemap):
    changefreq = "never"
    priority = 0.5

    def items(self):
        return models.Category.objects.filter(del_flg=False)

    def location(self, obj):
        return resolve_url('category', category_slug=obj.slug)

    def lastmod(self, obj):
        return obj.upate_date


class IndexSitemap(Sitemap):
    changefreq = "never"
    priority = 0.5

    def items(self):
        return models.Article.objects.filter(slug='top')

    def location(self, obj):
        return resolve_url('index')

    def lastmod(self, obj):
        return obj.create_date
