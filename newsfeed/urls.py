from django.conf.urls import patterns, url
# from newsfeed.views import index, detail
from newsfeed import views

urlpatterns = patterns('',
    url(r'^$', views.index, name='index'),
    url(r'^(?P<news_id>\d+)/$', views.detail, name='detail'),
    url(r'^tag/(?P<tag_name>.+)/$', views.news_bytag_name, name='news_bytag_name'),
    url(r'^cat/(?P<cat_id>\d+)/$', views.news_list, name='news_list')
)