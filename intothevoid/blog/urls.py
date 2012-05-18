#!/usr/bin/python
# -*- coding: utf-8 -*-

"""Definition of urls specific to this blog application.
"""

__author__ = "M. Ziemba"
__date__   = "2012-05-16, 23:09"

from django.conf.urls.defaults import patterns, url
from django.views.generic import ListView, DetailView, TemplateView
from django.contrib.syndication.views import Feed
from models import Post, Review


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
    url(r'^blog/$', ListView.as_view(
                               queryset=Post.objects.all().order_by("-created")[:10],
                               template_name="blog.html")),
    url(r'^blog/(?P<pk>\d+)$', DetailView.as_view(
                               model=Post,
                               template_name="post.html")),
    url(r'^reviews/$', ListView.as_view(
                               queryset=Review.objects.all().order_by("-added")[:10],
                               template_name="reviews.html")),
    url(r'^reviews/(?P<pk>\d+)$', DetailView.as_view(
                               model=Review,
                               template_name="review.html")),
    url(r'^archives/$', ListView.as_view(
                               queryset=Post.objects.all().order_by("-created"),
                               template_name="archives.html")),
    url(r'^shows/$', TemplateView.as_view(template_name="shows.html")),
    url(r'^links/$', TemplateView.as_view(template_name="links.html")),
    url(r'^contact/$', TemplateView.as_view(template_name="contact.html")),
    url(r'^tag/(?P<tag>\w+)$', 'tagpage'),
    url(r'^feed/$', BlogFeed())
)
