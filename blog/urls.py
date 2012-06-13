# -*- coding: utf-8 -*-

"""Definition of urls specific to this blog application."""

__author__ = "M. Ziemba"
__date__   = "2012-05-16, 23:09"

from django.conf.urls.defaults import patterns, url
from django.views.generic import ListView, DetailView, TemplateView

import views
from models import Post, Review
from feeds import BlogFeed


urlpatterns = patterns('blog.views',
    url(r'^blog/$', views.index),
    url(r'^blog/(?P<year>\d{4})$', views.archive_year),
    url(r'^blog/(?P<year>\d{4})/(?P<month>\d+)$', views.archive_month),
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
