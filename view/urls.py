from django.conf.urls import patterns, url

from view import views

urlpatterns = patterns('',
    url(r'^$', views.index, name='index'),
    url(r'^account/$', views.account, name='account'),
    url(r'^analysis/$', views.analysis, name='analysis'),
    url(r'^about/$', views.about, name='about'),
)