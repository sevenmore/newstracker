from django.conf.urls import patterns, include, url
from django.conf.urls.defaults import handler404, handler500
from django.conf import settings

# Uncomment the next two lines to enable the admin:
from django.contrib import admin
admin.autodiscover()

from view.views import error_404, error_500

urlpatterns = patterns('',
                       url(r'^', include("view.urls")),
                       url(r'^', include("login.urls")),
                       url(r'^admin/', include(admin.site.urls)),
                       )

handler500 = error_500
handler404 = error_404


#testing 404 and 500 pages
'''if settings.DEBUG:
    urlpatterns += patterns('',
        (r'^404/$', 'django.views.defaults.page_not_found'),
        (r'^500/$', 'django.views.defaults.server_error'),
    )'''
