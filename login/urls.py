from django.conf.urls import patterns, include, url
from django.contrib.auth.views import login, logout

from login import views

urlpatterns = patterns('', url(r'login/',
                       views.login, name='login'),
                       url(r'logout/', views.logout, name='logout'),
                       url(r'register/', views.register, name='register'),
                       )
