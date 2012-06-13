# -*- coding: utf-8 -*-

"""Definition of feeds."""

__author__ = "M. Ziemba"
__date__ = "2012-06-12, 00:28"

from django.contrib.syndication.views import Feed

from models import Post


class BlogFeed(Feed):
    """Class providing RSS feed.
    """

    title = "Metalurg Blog"
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
