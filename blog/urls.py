# -*- coding: utf-8 -*-

"""Definition of urls specific to this blog application."""

__author__ = "M. Ziemba"
__date__   = "2012-05-16, 23:09"

from django.conf.urls.defaults import patterns, url, include
from django.contrib.auth.views import login

import views
from feeds import BlogFeed
from utils import get_extra_context


urlpatterns = patterns('blog.views',
    url(r'^login/$', login, {'template_name': 'login.html', 'extra_context': get_extra_context()}),
    url(r'^logout/$', views.logout_view),
    url(r'^register/$', views.register),
    url(r'^blog/$', views.posts_index),
    url(r'^blog/archives/(?P<year>\d{4})$', views.archive_year),
    url(r'^blog/archives/(?P<year>\d{4})/(?P<month>\d+)$', views.archive_month),
    url(r'^blog/(?P<post_id>\d+)$', views.posts_single, name='post_view'),
    url(r'^photos/$', views.photos_index),
    url(r'^games/$', views.games_index),
    url(r'^team/$', views.team_index),
    url(r'^links/$', views.links_index),
    url(r'^contact/$', views.contact_index),
    url(r'^tag/(?P<tag>\w+)$', 'tagpage'),
    url(r'^comments', include('django.contrib.comments.urls')),
    url(r'^feed/$', BlogFeed())
)
