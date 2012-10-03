from django.contrib import admin
from monitorings.models import Article, ArticleAdminForm, SliderImg, Params, TextBlock, Menu, MenuAdminForm, TextBlockAdminForm,  Supplement, Template, TemplateScreenshot, SupplementScreenshot


class ArticleAdmin(admin.ModelAdmin):
    form = ArticleAdminForm


class MenuAdmin(admin.ModelAdmin):
    form = MenuAdminForm

    class Media:
        js = ("/static/js/tinymce/jscripts/tiny_mce/tiny_mce.js",
              "/static/js/init_tiny_mce.js",)


class TextBlockAdmin(admin.ModelAdmin):
    form = TextBlockAdminForm

    class Media:
        js = ("/static/js/tinymce/jscripts/tiny_mce/tiny_mce.js",
              "/static/js/init_tiny_mce.js",)


class SliderImgAdmin(admin.ModelAdmin):
    list_display = ('admin_image', 'img')


admin.site.register(Article, ArticleAdmin)
admin.site.register(SliderImg, SliderImgAdmin)
admin.site.register(Params)
admin.site.register(TextBlock, TextBlockAdmin)
admin.site.register(Menu, MenuAdmin)
admin.site.register(Supplement)
admin.site.register(Template)
admin.site.register(TemplateScreenshot)
admin.site.register(SupplementScreenshot)
