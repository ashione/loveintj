from django.conf.urls import patterns, include, url
from lover import views
urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'loveintj.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),
    #url(r'^login/$', views.login,name='login'),
    url(r'^$', views.index,name='index'),
)
