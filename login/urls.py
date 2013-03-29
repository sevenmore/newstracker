from django.conf.urls import patterns, url
from django.contrib.auth.views import login, logout

from login import views

urlpatterns = patterns('',
    #url(r'^$', views.login, name='login'),
)