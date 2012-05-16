#!/usr/bin/python
# -*- coding: utf-8 -*-

"""Definition of urls specific to this blog application.
"""

__author__ = "M. Ziemba"
__date__   = "2012-05-16, 23:09"

from django.conf.urls.defaults import patterns, url
from django.views.generic import ListView, DetailView
from django.contrib.syndication.views import Feed
from models import Post


class BlogFeed(Feed):
    """Class providing RSS feed.
    """

    title = "IntoTheVoid"
    description = "Blog about music"
    link = "/blog/feed/"

    def items(self):
        return Post.objects.all().order_by("-created")[:2]
    def item_title(self, item):
        return item.title
    def item_description(self, item):
        return item.body
    def item_link(self, item):
        return u'/blog/%d' % item.id

urlpatterns = patterns('blog.views',
    url(r'^$', ListView.as_view(
                               queryset=Post.objects.all().order_by("-created")[:2],
                               template_name="blog.html")),
    url(r'^(?P<pk>\d+)$', DetailView.as_view(
                               model=Post,
                               template_name="post.html")),
    url(r'^archives/$', ListView.as_view(
                               queryset=Post.objects.all().order_by("-created"),
                               template_name="archives.html")),
    url(r'^tag/(?P<tag>\w+)$', 'tagpage'),
    url(r'^feed/$', BlogFeed())
)
