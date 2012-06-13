# -*- coding: utf-8 -*-

"""Definition of urls specific to this blog application."""

__author__ = "M. Ziemba"
__date__   = "2012-05-16, 23:09"

from django.conf.urls.defaults import patterns, url
from django.views.generic import DetailView

import views
from models import Post
from feeds import BlogFeed


urlpatterns = patterns('blog.views',
    url(r'^blog/$', views.index),
    url(r'^blog/archives/(?P<year>\d{4})$', views.archive_year),
    url(r'^blog/archives/(?P<year>\d{4})/(?P<month>\d+)$', views.archive_month),
    url(r'^blog/(?P<pk>\d+)$', DetailView.as_view(
                               model=Post,
                               template_name="post.html")),
    url(r'^photos/$', views.photos_index),
    url(r'^team/$', views.team_index),
    url(r'^links/$', views.links_index),
    url(r'^contact/$', views.contact_index),
    url(r'^tag/(?P<tag>\w+)$', 'tagpage'),
    url(r'^feed/$', BlogFeed())
)
