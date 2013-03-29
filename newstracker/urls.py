from django.conf.urls import patterns, include, url
from django.conf.urls.defaults import handler404, handler500
from django.conf import settings

# Uncomment the next two lines to enable the admin:
from django.contrib import admin
admin.autodiscover()

from view.views import index, account, analysis, about, error_404, error_500
from login.views import logout, login, register

urlpatterns = patterns('',
    url(r'^$', index, name='index'),
    url(r'^admin/', include(admin.site.urls)),
    url(r'^account/$', account, name='account'),
    url(r'^login/$', login, name='login'),
    url(r'^logout/$', logout, name='logout'),
    url(r'^register/$', register, name='register'),

)

handler500 = error_500
handler404 = error_404


#testing 404 and 500 pages
'''if settings.DEBUG:
    urlpatterns += patterns('',
        (r'^404/$', 'django.views.defaults.page_not_found'),
        (r'^500/$', 'django.views.defaults.server_error'),
    )'''