# -*- coding: utf-8 -*-
from django.shortcuts import render_to_response, redirect
from monitorings.models import SliderImg, Article, Menu, TextBlock
from django.contrib import messages, auth

from loginza import signals, models
from loginza.templatetags.loginza_widget import _return_path
from django import http
from django.template.context import RequestContext
from django.contrib.auth.decorators import login_required

from .forms import CompleteReg


def loginza_auth_handler(sender, user, identity, **kwargs):
    try:
        models.UserMap.objects.get(user=user, verified=True)
        auth.login(sender, user)
    except models.UserMap.DoesNotExist:
        sender.session['users_complete_reg_id'] = identity.id
        return redirect('/complete_registration/')

signals.authenticated.connect(loginza_auth_handler)


def complete_registration(request):
        if request.user.is_authenticated():
            return http.HttpResponseForbidden(u'Вы попали сюда по ошибке')
        try:
            identity_id = request.session.get('users_complete_reg_id', None)
            user_map = models.UserMap.objects.get(identity__id=identity_id)
        except models.UserMap.DoesNotExist:
            return http.HttpResponseForbidden(u'Вы попали сюда по ошибке')
        if request.method == 'POST':
            form = CompleteReg(user_map.user.id, request.POST)
            if form.is_valid():
                user_map.user.username = form.cleaned_data['username']
                user_map.user.email = form.cleaned_data['email']
                user_map.user.save()

                user_map.verified = True
                user_map.save()

                user = auth.authenticate(user_map=user_map)
                auth.login(request, user)

                messages.info(request, u'Добро пожаловать!')
                del request.session['users_complete_reg_id']
                return redirect(_return_path(request))
        else:
            form = CompleteReg(user_map.user.id, initial={'username': user_map.user.username, 'email': user_map.user.email})
        return render_to_response('registration/complete_reg.html',
               {'form': form},
               context_instance=RequestContext(request),)


@login_required
def profile(request):
    return render_to_response('registration/profile.html', {'user': request.user}, context_instance=RequestContext(request))


def home(request):
    slider_img = SliderImg.objects.all()
    main_text_block = None
    main_text_blocks = TextBlock.objects.filter(is_main=1)
    print dir(request.session)
    print request.session.get('users_complete_reg_id', None)

    if main_text_blocks:
        main_text_block = main_text_blocks[0]
    return render_to_response('main.html', {'slider_img': slider_img, 'main_text_block': main_text_block}, context_instance=RequestContext(request))


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
