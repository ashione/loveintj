from django.conf.urls import patterns, include, url
from . import views
urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'loveintj.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),
    url(r'^index/$', views.login),
)
