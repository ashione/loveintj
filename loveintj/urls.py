from django.conf.urls import patterns, include, url
from django.conf.urls.static import static
from django.contrib import admin
import settings
#import lover.urls as lurls
#from lover import *
admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'loveintj.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),
    url(r'^$', 'lover.views.index'),
    url(r'^love/', include('lover.urls',namespace="lover")),
    #url(r'^$', 'loveintj.views.index', name=''),
    url(r'^admin/', include(admin.site.urls)),
    url(r'^login/', 'lover.views.login'),
)
#urlpatterns += [
#    url(r'^/love/', include(lurls)),
#]

if settings.DEBUG and settings.STATIC_ROOT:
#if settings.STATIC_ROOT:
    urlpatterns += static(settings.STATIC_URL,
    document_root=settings.STATIC_ROOT)

if settings.DEBUG is False:
    urlpatterns += patterns('',
    url(r'^static/(?P<path>.*)$', 'django.views.static.serve', {
        'document_root': settings.STATIC_ROOT,
    }),
)

