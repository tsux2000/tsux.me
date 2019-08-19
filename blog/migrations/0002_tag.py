# Generated by Django 2.2.4 on 2019-08-19 06:15

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Tag',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('slug', models.SlugField(max_length=255, unique=True, verbose_name='タグID')),
                ('name', models.CharField(max_length=255, verbose_name='タグ名')),
                ('create_date', models.DateField(default=django.utils.timezone.now, verbose_name='作成日')),
                ('del_flg', models.BooleanField(default=False, verbose_name='削除')),
            ],
            options={
                'verbose_name_plural': 'カテゴリ',
            },
        ),
    ]