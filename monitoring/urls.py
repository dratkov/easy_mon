from django.conf.urls import patterns, include, url
from django.conf import settings
# Uncomment the next two lines to enable the admin:
from django.contrib import admin
from monitoring.views import profile, home, news, page_from_menu
admin.autodiscover()


urlpatterns = patterns('',
    url(r'^accounts/', include('registration.urls')),
    (r'^accounts/profile/', profile),
    (r'^news/(\d+?)?\/?$', news),
    (r'^pages/(\d+)\/?$', page_from_menu),
    # Examples:
    url(r'^$', 'monitoring.views.home', name='home'),
    # url(r'^monitoring/', include('monitoring.foo.urls')),

    # Uncomment the admin/doc line below to enable admin documentation:
    # url(r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
    url(r'^admin/', include(admin.site.urls)),
)

if settings.DEBUG:
    urlpatterns += patterns('',
        url(r'^media/(?P<path>.*)$', 'django.views.static.serve', {
        'document_root': settings.MEDIA_ROOT,
        }),
    )
