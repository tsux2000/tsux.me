
from blog import models
from django.contrib.sitemaps import Sitemap
from django.shortcuts import resolve_url

import datetime

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
        articles = obj.article_set.all().order_by('-update_date')
        if articles:
            return articles[0].update_date
        else:
            return obj.create_date


class IndexSitemap(Sitemap):
    changefreq = "never"
    priority = 0.5

    def items(self):
        return [{
            'url': resolve_url('index'),
            'update': datetime.datetime(2020, 2, 1)
        }]

    def location(self, obj):
        return obj['url']

    def lastmod(self, obj):
        return obj['update']
