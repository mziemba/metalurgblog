# -*- coding: utf-8 -*-

"""Definition of views used by app.
"""

__author__ = "M. Ziemba"
__date__   = "2012-05-16, 23:11"

import datetime
import logging

from django.template import RequestContext
from django.shortcuts import render_to_response

from models import Post
from utils import get_archive_posts

_LOGGER = logging.getLogger('blog.custom')


def tagpage(request, tag):
    """View responsible for showing all posts for given tag.

    Args:
        request -- request
        tag -- tag by which we filter
    """
    posts = Post.objects.filter(tags__name=tag)
    return render_to_response("tagpage.html", {"posts": posts, "tag": tag})

def contactpage(request):
    return render_to_response("contact.html")

def index(request):
    """Views main blog page.
    """
    posts = Post.objects.filter().order_by('-created')
    now = datetime.datetime.now()

    archive_posts = get_archive_posts(posts)

    _LOGGER.debug("Posts archive dict: %s", str(archive_posts))

    return render_to_response("blog.html", {"posts": posts, "now": now,
                                            "list_events": archive_posts},
                              context_instance=RequestContext(request))
