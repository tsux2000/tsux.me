from django.urls import path
from blog.views import ArticleView, ArticleListView

urlpatterns = [
    path('', ArticleListView.as_view(), name='list'),
    path('category/<slug:category_slug>/', ArticleListView.as_view(), name='list'),
    path('<slug:article_slug>/', ArticleView.as_view(), name='article'),
]
