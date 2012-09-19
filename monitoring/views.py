# -*- coding: utf-8 -*-
from django.shortcuts import render_to_response
from monitorings.models import SliderImg, Article, Menu
from django.template import RequestContext


def profile(request):
    return render_to_response('registration/profile.html', {'user': request.user}, context_instance=RequestContext(request))


def home(request):
    slider_img = SliderImg.objects.all()
    return render_to_response('main.html', {'slider_img': slider_img}, context_instance=RequestContext(request))


def news(request, news_id):
    if news_id == None:
        news_id = 0
    news_id = int(news_id)
    article = None
    list_article = None
    if news_id > 0:
        article = Article.objects.get(id=news_id)
    else:
        list_article = Article.objects.order_by('-date_published')
    return render_to_response('news.html', {'list_article': list_article, 'article': article, 'news_id': news_id}, context_instance=RequestContext(request))


def page_from_menu(request, page_id):
    page_from_menu = Menu.objects.get(id=page_id)
    return render_to_response('page_from_menu.html', {'page_from_menu': page_from_menu}, context_instance=RequestContext(request))
