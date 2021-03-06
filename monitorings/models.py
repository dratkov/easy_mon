# -*- coding: utf-8 -*-
from django.db import models
from django.forms import ModelForm, Textarea


class Article(models.Model):
    title = models.CharField(max_length=50, verbose_name='Заголовок')
    published = models.BooleanField(verbose_name='Опубликовать')
    anons = models.CharField(max_length=250, verbose_name='Анонс')
    text = models.TextField(verbose_name='Текст')
    date_published = models.DateField(verbose_name='Дата публикации')

    def __unicode__(self):
        return self.title

    class Meta:
        verbose_name = "Статья"
        verbose_name_plural = "Статьи"


class ArticleAdminForm(ModelForm):
    class Meta:
          model = Article
          widgets = {
               'anons': Textarea(attrs={'cols': 50, 'rows': 5}),
          }


class SliderImg(models.Model):
    img = models.FileField(upload_to='slider_img', verbose_name="Картинка для галлереи")

    def admin_image(self):
        return '<img height="40" width="50" src="/media/%s"/>' % self.img
    admin_image.allow_tags = True

    class Meta:
        verbose_name = "Картинки для слайдера"
        verbose_name_plural = "Картинки для слайдера"


class Params(models.Model):
    key = models.CharField(max_length=50, verbose_name="Ключ")
    value = models.CharField(max_length=100, verbose_name="Значение")

    class Meta:
        verbose_name = "Параметры контента"
        verbose_name_plural = "Параметры контента"

    def __unicode__(self):
        return self.key


class Transaction(models.Model):
    user_id = models.IntegerField()
    completed = models.BooleanField()
    date_created = models.DateTimeField(auto_now=True)
    summa = models.SmallIntegerField()


class TextBlock(models.Model):
    text = models.TextField(verbose_name="Текст")
    title = models.CharField(max_length=100, verbose_name="Заголовок блока")
    is_main = models.BooleanField(verbose_name="Большой блок на главной странице")

    def __unicode__(self):
        return self.title

    class Meta:
        verbose_name = "Текстовый блок"
        verbose_name_plural = "Текстовые блоки"


class TextBlockAdminForm(ModelForm):
    class Meta:
          model = TextBlock
          widgets = {
               'text': Textarea(attrs={'cols': 120, 'rows': 30}),
          }


class Menu(models.Model):
    title = models.CharField(verbose_name="Заголовок", max_length="100")
    text = models.TextField(verbose_name="Текст или ссылка", blank=True)
    href = models.CharField(verbose_name="Меню - ссылка", max_length="200", blank=True)
    order = models.SmallIntegerField(verbose_name="Порядок сортировки в меню, целое число от 0 до 20, с большим числом в начале")

    def __unicode__(self):
        return self.title

    class Meta:
        verbose_name = "Главное меню"
        verbose_name_plural = "Главное меню"


class MenuAdminForm(ModelForm):
    class Meta:
          model = Menu
          widgets = {
               'text': Textarea(attrs={'cols': 120, 'rows': 30}),
          }

class SupplementScreenshot(models.Model):
    title = models.CharField(verbose_name="Название", max_length="100")
    small_img = models.ImageField(upload_to="template_screenshot", verbose_name="Маленькая картинка")
    big_img = models.ImageField(upload_to="template_screenshot", verbose_name="Оригинальный размер")

    def __unicode__(self):
        return self.title

    class Meta:
        verbose_name = "Скриншот для дополнений"
        verbose_name_plural = "Скриншоты для дополнений"


class Supplement(models.Model):
    title = models.CharField(verbose_name="Название", max_length="100")
    icon = models.ImageField(upload_to='supplement_icon', verbose_name="Иконка")
    updated = models.DateField(verbose_name="Дата обновления")
    buy_count = models.SmallIntegerField(verbose_name="Кол-во покупок", blank=True)
    version = models.CharField(max_length="50", verbose_name="Версия")
    short_description = models.CharField(max_length="250", verbose_name="Краткое описание")
    description = models.TextField(verbose_name="Описание")
    price = models.SmallIntegerField(verbose_name="Цена, в рублях, целое число")
    key = models.CharField(max_length="100", verbose_name="Ключик")
    screenshots = models.ManyToManyField(SupplementScreenshot)

    def __unicode__(self):
        return self.title

    class Meta:
        verbose_name = "Дополнение"
        verbose_name_plural = "Дополнения"


class TemplateScreenshot(models.Model):
    title = models.CharField(verbose_name="Название", max_length="100")
    small_img = models.ImageField(upload_to="template_screenshot", verbose_name="Маленькая картинка")
    big_img = models.ImageField(upload_to="template_screenshot", verbose_name="Оригинальный размер")

    def __unicode__(self):
        return self.title

    class Meta:
        verbose_name = "Скриншот для шаблонов"
        verbose_name_plural = "Скриншоты для шаблонов"


class Template(models.Model):
    title = models.CharField(verbose_name="Название", max_length="100")
    icon = models.ImageField(upload_to='template_icon', verbose_name="Иконка")
    updated = models.DateField(verbose_name="Дата обновления")
    buy_count = models.SmallIntegerField(verbose_name="Кол-во скачиваний", blank=True)
    version = models.CharField(max_length="50", verbose_name="Версия")
    short_description = models.CharField(max_length="250", verbose_name="Краткое описание")
    description = models.TextField(verbose_name="Описание")
    price = models.SmallIntegerField(verbose_name="Цена, в рублях, целое число")
    template_file = models.FileField(upload_to="templates", verbose_name="Файл")
    screenshots = models.ManyToManyField(TemplateScreenshot)
    def __unicode__(self):
        return self.title

    class Meta:
        verbose_name = "Шаблон"
        verbose_name_plural = "Шаблоны"


