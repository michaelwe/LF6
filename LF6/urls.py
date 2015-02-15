from django.conf.urls import patterns, include, url
from django.contrib import admin

urlpatterns = patterns('',
    url(r'^manage/', include('management.urls')),
    url(r'^admin/', include(admin.site.urls)),
)
