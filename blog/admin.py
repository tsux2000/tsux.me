from django.contrib import admin
from markdownx.admin import MarkdownxModelAdmin
from blog.models import Article, Category

admin.site.register(Article, MarkdownxModelAdmin)
admin.site.register(Category)
