# -*- coding: utf-8 -*-
from monitorings.models import Menu, Article


def my_global_vars(request):
    menu_res = Menu.objects.order_by('-order')
    last_article = Article.objects.order_by('-date_published')[:3]
    return {
            'site_title': u"Мониторинг", 'menu_res': menu_res, 'last_article': last_article
    }
