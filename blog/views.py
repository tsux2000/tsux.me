from django.views.generic import TemplateView
from django.shortcuts import redirect, render
from .func import *

class ArticleView(TemplateView):

    def get(self, request, article_slug):

        # セッション情報の初期化
        init_session(request)

        # 記事の取得
        article = get_article(article_slug)

        # 表示する記事が決定したところで記事の view 数の計算
        count_view(request, article)

        # テンプレートに渡すパラメータの用意
        param = {
            'meta': article,
            'article': article,
            'categories': get_category_list(),
            'tags': get_tag_list(),
        }

        return render(request, 'blog/index.html', param)

class ArticleListView(TemplateView):

    def get(self, request, category_slug='', yyyy_mm=''):

        page_no = request.GET.get('page_no') if 'page_no' in request.GET else 1
        order = request.GET.get('order') if 'order' in request.GET else '-create_date'
        tag_slug = request.GET.get('tag') if 'tag' in request.GET else ''
        keywords = request.GET.get('keywords') if 'keywords' in request.GET else ''

        article_list = get_article_list(category_slug, yyyy_mm, page_no, order)

        if keywords or tag_slug:
            keys =  keywords.replace('　', ' ').split()
            tag = get_tag(tag_slug) if tag_slug else ''
            category = get_category(category_slug) if category_slug else ''
            article_list = search_articles(keys, category, tag, page_no, order)
            title = '絞り込み検索結果'
        elif category_slug:
            category = get_category(category_slug)
            title = '{} の記事一覧'.format(category.name)
        elif yyyy_mm:
            year = yyyy_mm.split('_')[0]
            month = yyyy_mm.split('_')[1] + '月' if '_' in yyyy_mm else ''
            title = "{0}年{1}の記事一覧".format(year, month)
        else:
            title= 'TOP'

        meta = {
            'slug': 'list',
            'robots': 'noindex, follow',
            'page_type': 'website',
            'description': 'どうも、情報系学生の tsux といいます。 何かと知識の整理をする必要が増えたので、 ポートフォリオにもなるかなと思い、どうせなら、とブログを作りました。 日々の学びを記録したり、知識の整理のために書いていこうと思います。 IT 関連を勉強しようと思っている読者の方の参考になれば幸いです。',
            'title': title,
            'thumbnail': {'url': ''},
        }

        # テンプレートに渡すパラメータの用意
        param = {
            'meta': meta,
            'article_list': article_list,
            'article_number': get_article_number(article_list, page_no, order),
            'categories': get_category_list(),
            'tags': get_tag_list(),
        }

        return render(request, 'blog/list.html', param)

