# -*- coding: utf-8 -*-
from monitorings.models import Menu, Article, TextBlock


def my_global_vars(request):
    menu_res = Menu.objects.order_by('-order')
    last_article = Article.objects.order_by('-date_published')[:3]
    text_blocks = TextBlock.objects.filter(is_main=0)
    page_title = u"Мониторинг"
    if len(request.path) > 1:
        for m in menu_res:
            if request.path.split('/')[1] == m.href.split('/')[1]:
                page_title = m.title + " &ndash; " + page_title
                break

    return {
            'site_title': page_title, 'menu_res': menu_res, 'last_article': last_article, 'text_blocks': text_blocks
    }
