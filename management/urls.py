from django.conf.urls import patterns, include, url
from django.contrib import admin

urlpatterns = patterns('',
    url(r'^$', 'management.views.show_users', name='show_users'),
    # url(r'^blog/', include('blog.urls')),
)
