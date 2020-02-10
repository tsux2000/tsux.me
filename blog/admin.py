
from blog import models
from django.contrib import admin
from markdownx.admin import MarkdownxModelAdmin

admin.site.register(models.Article, MarkdownxModelAdmin)
admin.site.register(models.Category)
admin.site.register(models.Comment, MarkdownxModelAdmin)
admin.site.register(models.Author)
admin.site.register(models.Advertisement)
