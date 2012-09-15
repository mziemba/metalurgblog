#!/usr/bin/python
# -*- coding: utf-8 -*-

"""Main url definitions for application."""

__author__ = "M. Ziemba"
__date__ = "2012-05-15, 23:01"

from django.conf.urls.defaults import patterns, include, url

from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    url(r'^', include('blog.urls')),
    url(r'^admin/', include(admin.site.urls)),
)

handler500 = 'metalurgblog.blog.views.server_error'
handler404 = 'metalurgblog.blog.views.page_not_found'