# Generated by Django 2.2.4 on 2019-08-19 05:14

from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Article',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('slug', models.SlugField(max_length=255, unique=True, verbose_name='記事ID')),
                ('robots', models.CharField(default='index, follow', max_length=255, verbose_name='クローラ設定')),
                ('page_type', models.CharField(default='article', max_length=255, verbose_name='ページタイプ')),
                ('description', models.TextField(blank=True, verbose_name='説明')),
                ('title', models.CharField(max_length=255, verbose_name='タイトル')),
                ('contents', models.TextField(verbose_name='コンテンツ')),
                ('create_date', models.DateField(default=django.utils.timezone.now, verbose_name='作成日')),
                ('update_date', models.DateField(auto_now=True, verbose_name='更新日')),
                ('views', models.IntegerField(default=0, verbose_name='閲覧数')),
                ('thumbnail', models.ImageField(blank=True, upload_to='thumbnail', verbose_name='サムネイル')),
                ('private_flg', models.BooleanField(default=False, verbose_name='非公開')),
                ('del_flg', models.BooleanField(default=False, verbose_name='削除')),
            ],
            options={
                'verbose_name_plural': '記事',
            },
        ),
        migrations.CreateModel(
            name='Attachment',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('slug', models.SlugField(max_length=255, unique=True, verbose_name='ファイルID')),
                ('file', models.ImageField(blank=True, upload_to='uploads', verbose_name='添付ファイル')),
                ('upload_date', models.DateField(default=django.utils.timezone.now, verbose_name='アップロード日')),
            ],
            options={
                'verbose_name_plural': '添付ファイル',
            },
        ),
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('slug', models.SlugField(max_length=255, unique=True, verbose_name='カテゴリID')),
                ('name', models.CharField(max_length=255, verbose_name='カテゴリ名')),
                ('create_date', models.DateField(default=django.utils.timezone.now, verbose_name='作成日')),
                ('del_flg', models.BooleanField(default=False, verbose_name='削除')),
            ],
            options={
                'verbose_name_plural': 'カテゴリ',
            },
        ),
        migrations.CreateModel(
            name='Comment',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('from_user', models.CharField(max_length=255, verbose_name='ユーザ名')),
                ('contents', models.TextField(verbose_name='内容')),
                ('create_date', models.DateField(default=django.utils.timezone.now, verbose_name='コメント日')),
                ('del_flg', models.BooleanField(default=False, verbose_name='削除')),
                ('article', models.ForeignKey(blank=True, on_delete=django.db.models.deletion.CASCADE, to='blog.Article', verbose_name='記事')),
            ],
            options={
                'verbose_name_plural': 'コメント',
            },
        ),
        migrations.AddField(
            model_name='article',
            name='category',
            field=models.ForeignKey(blank=True, on_delete=django.db.models.deletion.CASCADE, to='blog.Category', verbose_name='カテゴリ'),
        ),
    ]
