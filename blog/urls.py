from django.urls import path
from blog.views import IndexView, ArticleView, ArticleListView

urlpatterns = [
    path('', IndexView.as_view(), name='index'),
    path('list/', ArticleListView.as_view(), name='list'),
    path('category/<slug:category_slug>/', ArticleListView.as_view(), name='category'),
    path('<slug:article_slug>/', ArticleView.as_view(), name='article'),
]
