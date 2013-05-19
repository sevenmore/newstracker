from django.conf.urls import patterns, include, url
from tastypie.api import Api
from view.resources import RssInRessource
from view import views

v1_api = Api(api_name='v1')
v1_api.register(RssInRessource())

urlpatterns = patterns('',
                       url(r'^account/$', views.account, name='account'),
                       url(r'^analysis/$', views.analysis, name='analysis'),
                       url(r'^about/$', views.about, name='about'),
                       url(r'viz/$', views.viz, name='viz'),
                       url(r'^api/', include(v1_api.urls)),
                       url(r'^rss/$', views.rss, name='rss'),
                       url(r'^$', views.index, name='index'),
                       )
