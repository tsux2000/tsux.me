from django.urls import path
from .views import ArticleView, ArticleListView

urlpatterns = [

    # canonical_url: 'blog/'
    path('', ArticleListView.as_view(), name='top'),
    # canonical_url: 'blog/article_slug/'
    path('<slug:article_slug>/', ArticleView.as_view(), name='article'),

    # canonical_url: 'blog/category/category_slug/'
    path('category/<slug:category_slug>/', ArticleListView.as_view(), name='list'),

    # canonical_url: 'blog/archive/yyyy_mm/'
    path('archive/<int:yyyy_mm>/', ArticleListView.as_view(), name='list'),

]
