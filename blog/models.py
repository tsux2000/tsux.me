from django.db import models
from django.utils import timezone

class Article(models.Model):
    """Article model"""

    slug = models.SlugField(verbose_name='記事ID', max_length=255, unique=True,)
    title = models.CharField(verbose_name='タイトル', max_length=255,)
    description = models.TextField(verbose_name='概要',)
    contents = models.TextField(verbose_name='コンテンツ',)
    category = models.ForeignKey('Category', verbose_name='カテゴリ', blank=True, on_delete=models.CASCADE,)
    tag = models.ManyToManyField('Tag', verbose_name='タグ', blank=True,)
    create_date = models.DateField(verbose_name='作成日', default=timezone.now,)
    update_date = models.DateField(verbose_name='更新日', auto_now=True,)
    views = models.IntegerField(verbose_name='閲覧数', default=0,)
    thumbnail = models.ImageField(verbose_name='サムネイル', blank=True, upload_to='thumbnail')
    private_flg = models.BooleanField(verbose_name='非公開', default=False,)
    del_flg = models.BooleanField(verbose_name='削除', default=False,)

    def __str__(self):
        return self.title + "(" + self.slug + ")"

    class Meta:
        verbose_name_plural = '記事'

class Attachment(models.Model):
    """Attachment model"""

    slug = models.SlugField(verbose_name='ファイルID', max_length=255, unique=True,)
    file = models.ImageField(verbose_name='添付ファイル', blank=True, upload_to='uploads')
    upload_date = models.DateField(verbose_name='アップロード日', default=timezone.now,)

    def __str__(self):
        return self.slug

    class Meta:
        verbose_name_plural = '添付ファイル'


class Category(models.Model):
    """Category model"""

    slug = models.SlugField(verbose_name='カテゴリID', max_length=255, unique=True,)
    name = models.CharField(verbose_name='カテゴリ名', max_length=255,)
    create_date = models.DateField(verbose_name='作成日', default=timezone.now,)
    del_flg = models.BooleanField(verbose_name='削除', default=False,)

    def __str__(self):
        return self.name + "(" + self.slug + ")"

    class Meta:
        verbose_name_plural = 'カテゴリ'


class Tag(models.Model):
    """Tag model"""

    slug = models.SlugField(verbose_name='タグID', max_length=255, unique=True,)
    name = models.CharField(verbose_name='タグ名', max_length=255,)
    create_date = models.DateField(verbose_name='作成日', default=timezone.now,)
    del_flg = models.BooleanField(verbose_name='削除', default=False,)

    def __str__(self):
        return self.name + "(" + self.slug + ")"

    class Meta:
        verbose_name_plural = 'タグ'
