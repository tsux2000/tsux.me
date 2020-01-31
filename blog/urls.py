
from blog import views
from django.urls import path

urlpatterns = [
    path('', views.IndexView.as_view(), name='index'),
    path('list/', views.ArticleListView.as_view(), name='list'),
    path('category/<slug:category_slug>/', views.ArticleListView.as_view(), name='category'),
    path('comment/', views.CommentView.as_view(), name='comment'),
    path('<slug:article_slug>/', views.ArticleView.as_view(), name='article'),
]
