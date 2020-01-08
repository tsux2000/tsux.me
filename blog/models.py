import re
import uuid
from django.db import models
from django.utils import timezone
from markdownx.models import MarkdownxField
from markdownx.utils import markdownify


class Article(models.Model):

    slug = models.SlugField(verbose_name='記事ID', max_length=255, unique=True,)
    contents = MarkdownxField(verbose_name='コンテンツ',)
    category = models.ForeignKey('Category', verbose_name='カテゴリ', blank=True, null=True, on_delete=models.CASCADE,)
    create_date = models.DateField(verbose_name='作成日', default=timezone.now,)
    update_date = models.DateField(verbose_name='更新日', auto_now=True,)
    views = models.IntegerField(verbose_name='閲覧数', default=0,)
    del_flg = models.BooleanField(verbose_name='削除', default=False,)

    def __str__(self):
        return self.title

    @property
    def title(self):
        title = re.search(r'<h1.*?>(.*)</h1>', markdownify(self.contents))
        return title.groups()[0] if title else ''

    @property
    def thumbnail(self):
        image = re.search(r'<img.*?src="(.*)".*?>', markdownify(self.contents))
        return {'url':image.groups()[0]} if image else None

    @property
    def get_markdown(self):
        return markdownify(self.contents)

    class Meta:
        verbose_name = 'Article'
        verbose_name_plural = 'Articles'


class Category(models.Model):

    slug = models.SlugField(verbose_name='カテゴリID', max_length=255, unique=True,)
    name = models.CharField(verbose_name='カテゴリ名', max_length=255,)
    create_date = models.DateField(verbose_name='作成日', default=timezone.now,)
    del_flg = models.BooleanField(verbose_name='削除', default=False,)

    def __str__(self):
        return self.name + "(" + self.slug + ")"

    class Meta:
        verbose_name = 'Category'
        verbose_name_plural = 'Categories'
