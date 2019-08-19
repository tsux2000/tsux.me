from django.db import models
from django.utils import timezone

# 記事モデル
class Article(models.Model):
    """`Article` model"""

    slug = models.SlugField(verbose_name='記事ID', max_length=255, unique=True,)
    robots = models.CharField(verbose_name='クローラ設定', max_length=255, default='index, follow')
    page_type = models.CharField(verbose_name='ページタイプ', max_length=255, default='article')
    description = models.TextField(verbose_name='説明', blank=True, )
    title = models.CharField(verbose_name='タイトル', max_length=255,)
    contents = models.TextField(verbose_name='コンテンツ', )
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

# 添付ファイル保存用モデル
class Attachment(models.Model):
    """`Attachment` model"""

    slug = models.SlugField(verbose_name='ファイルID', max_length=255, unique=True,)
    file = models.ImageField(verbose_name='添付ファイル', blank=True, upload_to='uploads')
    upload_date = models.DateField(verbose_name='アップロード日', default=timezone.now,)

    def __str__(self):
        return self.slug

    class Meta:
        verbose_name_plural = '添付ファイル'

# カテゴリモデル
class Category(models.Model):
    """`Category` model"""

    slug = models.SlugField(verbose_name='カテゴリID', max_length=255, unique=True,)
    name = models.CharField(verbose_name='カテゴリ名', max_length=255,)
    create_date = models.DateField(verbose_name='作成日', default=timezone.now,)
    del_flg = models.BooleanField(verbose_name='削除', default=False,)

    def __str__(self):
        return self.name + "(" + self.slug + ")"

    class Meta:
        verbose_name_plural = 'カテゴリ'

# コメントモデル
class Comment(models.Model):
    """`Comment` model"""

    from_user = models.CharField(verbose_name='ユーザ名', max_length=255,)
    article = models.ForeignKey('Article', verbose_name='記事',  blank=True,on_delete=models.CASCADE,)
    contents = models.TextField(verbose_name='内容', )
    create_date = models.DateField(verbose_name='コメント日', default=timezone.now,)
    del_flg = models.BooleanField(verbose_name='削除', default=False,)

    def __str__(self):
        return self.from_user + "「" + self.contents[0:10] + "…」 (" + self.pk + ")"

    class Meta:
        verbose_name_plural = 'コメント'

# タグモデル
class Tag(models.Model):
    """`Tag` model"""

    slug = models.SlugField(verbose_name='タグID', max_length=255, unique=True,)
    name = models.CharField(verbose_name='タグ名', max_length=255,)
    create_date = models.DateField(verbose_name='作成日', default=timezone.now,)
    del_flg = models.BooleanField(verbose_name='削除', default=False,)

    def __str__(self):
        return self.name + "(" + self.slug + ")"

    class Meta:
        verbose_name_plural = 'カテゴリ'
