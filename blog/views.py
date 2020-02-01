
from blog import models, forms
from django.db.models import Q
from django.http import Http404
from django.shortcuts import get_object_or_404, redirect
from django.utils import timezone
from django.views import generic

import datetime

class IndexView(generic.ListView):

    template_name = 'blog/index.html'
    categories = models.Category.objects.filter(del_flg=False)
    paginate_by = 6
    queryset = models.Article.objects.filter(del_flg=False).order_by('-create_date')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context.update({
            'meta': {'title': 'tsux.me',},
            'categories': self.categories,
            'dates': models.Article.objects.filter(create_date__lte=timezone.now()).dates('create_date', 'month', order='DESC'),
        })
        return context


class ArticleView(generic.DetailView):

    template_name = 'blog/article.html'
    categories = models.Category.objects.filter(del_flg=False)
    queryset = models.Article.objects.filter(del_flg=False)
    slug_field = 'slug'
    slug_url_kwarg = 'article_slug'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context.update({
            'meta': {'title': '{} | tsux.me'.format(self.object.title),},
            'title': self.object.title,
            'categories': self.categories,
            'dates': models.Article.objects.filter(create_date__lte=timezone.now()).dates('create_date', 'month', order='DESC'),
        })
        return context


class ArticleListView(generic.ListView):

    template_name = 'blog/list.html'
    categories = models.Category.objects.filter(del_flg=False)
    paginate_by = 6
    title = '記事一覧'

    def get_queryset(self):
        articles = models.Article.objects.filter(del_flg=False).order_by(self.request.GET.get('order', '-create_date'))
        category_slug = self.request.GET.get('category', self.kwargs.get('category_slug'))
        year_and_month = self.request.GET.get('archive', '').split('_')
        keywords = self.request.GET.get('keywords', '').replace('　', ' ').split()
        if len(year_and_month) == 2:
            articles = articles.filter(create_date__year=year_and_month[0], create_date__month=year_and_month[1])
            self.title = '{0[0]}年{0[1]}月のアーカイブ'.join(year_and_month)
        elif category_slug:
            category = get_object_or_404(self.categories, slug=category_slug)
            articles = articles.filter(category=category)
            self.title = '「{}」カテゴリ'.format(category.name)
        if keywords:
            for i in keywords:
                articles = articles.filter(Q(title__icontains=i) | Q(contents__icontains=i) | Q(description__icontains=i))
            self.title = '「{}」の検索結果'.format(' '.join(keywords))
        return articles

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context.update({
            'meta': {'title': '{} | tsux.me'.format(self.title),},
            'title': self.title,
            'categories': self.categories,
            'dates': models.Article.objects.filter(create_date__lte=timezone.now()).dates('create_date', 'month', order='DESC'),
        })
        return context


class CommentView(generic.View):

    def get(self, request):
        raise Http404

    def post(self, request):
        post_data = request.POST.copy()
        if not post_data.get('name'):
            post_data['name'] = '名無し'
        form = forms.CommentForm(post_data)
        if not form.is_valid():
            raise Http404
        article = get_object_or_404(models.Article, pk=post_data.get('article'))
        form.save()
        return redirect('article', article.slug)
