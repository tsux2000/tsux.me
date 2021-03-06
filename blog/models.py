
from django.db import models
from django.utils import timezone
from markdownx.models import MarkdownxField
from markdownx.utils import markdownify

import re

class Article(models.Model):
    slug = models.SlugField(verbose_name='記事ID', max_length=255, unique=True)
    contents = MarkdownxField(verbose_name='コンテンツ')
    category = models.ForeignKey('Category', verbose_name='カテゴリ', blank=True, null=True, on_delete=models.CASCADE)
    create_date = models.DateField(verbose_name='作成日', default=timezone.now)
    update_date = models.DateField(verbose_name='更新日', auto_now=True)
    del_flg = models.BooleanField(verbose_name='削除', default=False)

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


class Category(models.Model):
    slug = models.SlugField(verbose_name='カテゴリID', max_length=255, unique=True)
    name = models.CharField(verbose_name='カテゴリ名', max_length=255)
    create_date = models.DateField(verbose_name='作成日', default=timezone.now)
    update_date = models.DateField(verbose_name='更新日', auto_now=True)
    del_flg = models.BooleanField(verbose_name='削除', default=False)

    def __str__(self):
        return '{} ({})'.format(self.name, self.slug)

    class Meta:
        verbose_name_plural = 'Categories'


class Comment(models.Model):
    article = models.ForeignKey('Article', verbose_name='コメント先ノート', on_delete=models.CASCADE)
    parent = models.ForeignKey('self', verbose_name='返信', blank=True, null=True, on_delete=models.CASCADE)
    name = models.CharField(verbose_name='名前', max_length=255, default='名無し')
    contents = MarkdownxField(verbose_name='コンテンツ')
    create_date = models.DateTimeField(verbose_name='作成日', default=timezone.now)
    del_flg = models.BooleanField(verbose_name='削除', default=False)

    def __str__(self):
        return '{}...({}さん)'.format(self.contents[:20], self.name)

    @property
    def get_markdown(self):
        return markdownify(self.contents)

class Author(models.Model):
    name = models.CharField(verbose_name='表示名', max_length=255)
    icon = models.ImageField(verbose_name='アイコン', upload_to='author/icon.jpg', blank=True, null=True)
    bio = models.TextField(verbose_name='一言')
    create_date = models.DateField(verbose_name='作成日', default=timezone.now)
    update_date = models.DateField(verbose_name='更新日', auto_now=True)

    def __str__(self):
        return '{}'.format(self.name)

class Advertisement(models.Model):
    advertise_name = models.CharField(verbose_name='広告名', max_length=255, blank=True)
    affiliate_company_name = models.CharField(verbose_name='アフィリエイト会社', max_length=255, blank=True)
    advertise_company_name = models.CharField(verbose_name='広告会社', max_length=255, blank=True)
    image = models.ImageField(verbose_name='画像', upload_to='advertisement/', blank=True, null=True)
    code = models.TextField(verbose_name='コード')
    display_type = models.IntegerField(
        verbose_name='display type',
        choices=(
            (0, '300x300'),
            (1, '468x60'),
        ),
    )
    create_date = models.DateField(verbose_name='作成日', default=timezone.now)
    update_date = models.DateField(verbose_name='更新日', auto_now=True)
    del_flg = models.BooleanField(verbose_name='削除', default=False)

    def __str__(self):
        return '{}'.format(self.advertise_name)
