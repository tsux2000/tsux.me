import datetime
from blog.models import Article, Category, Tag
from django.utils import timezone
from django.db.models import Q
from django.shortcuts import get_object_or_404
from django.views.generic import TemplateView, ListView

class ArticleView(TemplateView):

    template_name = 'blog/index.html'
    categories = Category.objects.filter(del_flg=False)
    tags = Tag.objects.filter(del_flg=False)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        self.article = get_object_or_404(Article, slug=kwargs.get('article_slug'), private_flg=False, del_flg=False)
        self.process_session()
        base_url = self.request.scheme + '://' + self.request.get_host() + '/blog/'
        self.breadcrumb = [
            {'url': base_url, 'name': 'TOP'},
            {'url': base_url + 'category/' + self.article.category.slug + '/', 'name': self.article.category.name},
            {'url': base_url + self.article.slug + '/', 'name': self.article.title},
        ]
        context.update({
            'title': self.article.title,
            'breadcrumb': self.breadcrumb,
            'article': self.article,
            'categories': self.categories,
            'tags': self.tags,
            'dates': Article.objects.filter(create_date__lte=timezone.now()).dates('create_date', 'month', order='DESC'),
        })
        return context

    def process_session(self):
        if 'history' not in self.request.session:
            self.request.session['history'] = []
        log = [datetime.date.today().strftime('%Y-%m-%d'), self.article.pk]
        if log not in self.request.session['history']:
            self.article.views += 1
            self.article.save()
        self.request.session['history'].append(log)


class ArticleListView(ListView):

    template_name = 'blog/list.html'
    model = Article
    paginate_by = 6
    categories = Category.objects.filter(del_flg=False)
    tags = Tag.objects.filter(del_flg=False)
    title = '検索結果'
    breadcrumb = []

    def get_queryset(self):
        articles = self.model.objects.filter(private_flg=False, del_flg=False).order_by(self.request.GET.get('order', '-views'))
        category_slug = self.request.GET.get('category', self.kwargs.get('category_slug'))
        tag_slug = self.request.GET.get('tag', '')
        year_and_month = self.request.GET.get('archive', '').split('-')
        keywords = self.request.GET.get('keywords', '').replace('　', ' ').split()
        base_url = self.request.scheme + '://' + self.request.get_host() + '/blog/'
        self.breadcrumb = [{'url': base_url, 'name': 'TOP'}]
        if len(year_and_month) == 2:
            articles = articles.filter(create_date__year=year_and_month[0], create_date__month=year_and_month[1])
            self.breadcrumb.append({
                'url': base_url + '?archive=' + '-'.join(year_and_month),
                'name': '/'.join(year_and_month)
            })
            self.title = '年'.join(year_and_month) + '月のアーカイブ'
        elif category_slug:
            category = get_object_or_404(self.categories, slug=category_slug)
            articles = articles.filter(category=category)
            self.breadcrumb.append({
                'url': base_url + 'category/' + category.slug + '/',
                'name': '「' + category.name + '」カテゴリ'
            })
            self.title = '「' + category.name + '」カテゴリ'
        else:
            self.title = '記事一覧'
        if tag_slug:
            tag = get_object_or_404(self.tags, slug=tag_slug)
            articles = articles.filter(tag=tag)
            self.breadcrumb.append({
                'url': base_url + '?tag=' + tag.slug,
                'name': '「' + tag.name + '」タグ'
            })
            self.title = '検索結果'
        if keywords:
            for i in keywords:
                articles = articles.filter(Q(title__icontains=i) | Q(contents__icontains=i) | Q(description__icontains=i))
            self.breadcrumb.append({
                'url': base_url + '?keywords=' + ' '.join(keywords),
                'name': 'キーワード「' + ' '.join(keywords) + '」の記事'
            })
            self.title = '検索結果'
        return articles

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context.update({
            'title': self.title,
            'breadcrumb': self.breadcrumb,
            'categories': self.categories,
            'tags': self.tags,
            'dates': Article.objects.filter(create_date__lte=timezone.now()).dates('create_date', 'month', order='DESC'),
        })
        return context

