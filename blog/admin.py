from django.contrib import admin
from .models import Article, Attachment, Category, Comment, Tag

admin.site.register(Article)
admin.site.register(Attachment)
admin.site.register(Category)
admin.site.register(Comment)
admin.site.register(Tag)
