import datetime
from .models import Article, Category, Tag
from django.shortcuts import get_object_or_404
from django.db.models import Q

def count_view(request, article):
    log = [datetime.date.today().strftime('%m%d'), article.pk]
    if log not in request.session['view_history']:
        article.views += 1
        article.save()
    request.session['view_history'].append(log)

def get_article(slug):
    return get_object_or_404(Article, slug=slug, private_flg=False, del_flg=False)

def get_article_list(category='', yyyy_mm='', page_no=1, order='-create_date'):
    # 記事全体取得
    articles = Article.objects.filter(private_flg=False, del_flg=False)
    # カテゴリで絞り込み
    if category:
        articles = articles.filter(category__slug=category)
    # 時系列で絞り込み
    elif yyyy_mm:
        year = int(yyyy_mm.split('_')[0])
        month = int(yyyy_mm.split('_')[1]) if '_' in yyyy_mm else 0
        articles = articles.filter(update_date__year=year)
        if month:
            articles = articles.filter(update_date__month=month)
    offset = (int(page_no)-1)*10-1 if int(page_no)>1 else 0
    return articles.order_by(order)[offset:offset+10]

def get_article_number(article_list, page_no, order):
    offset = (int(page_no)-1)*10 if int(page_no)>1 else 1
    article_count = len(article_list)
    return '{}〜{}記事 / {}記事'.format(offset, min(offset+9, article_count) , article_count)

def get_category_list():
    return Category.objects.filter(del_flg=False)

def get_category(slug):
    return get_object_or_404(Category, slug=slug, del_flg=False)

def get_tag_list():
    return Tag.objects.filter(del_flg=False)

def get_tag(slug):
    return get_object_or_404(Tag, slug=slug, del_flg=False)

def init_session(request):
    if 'view_history' not in request.session:
        request.session['view_history'] = []

def search_articles(keys=[], category='', tag='', page_no=1, order='-create_date'):
    result = Article.objects.filter(private_flg=False, del_flg=False)
    if category:
        result = result.filter(category=category)
    if tag:
        result = result.filter(tag=tag)
    for i in keys:
        result = result.filter(Q(title__icontains=i) | Q(contents__icontains=i) | Q(description__icontains=i))
    offset = (int(page_no)-1)*10-1 if int(page_no)>1 else 0
    return result.order_by(order)[offset:offset+10]
