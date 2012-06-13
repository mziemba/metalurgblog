# -*- coding: utf-8 -*-

"""Definition of views used by blog app."""

__author__ = "M. Ziemba"
__date__   = "2012-05-16, 23:11"

import datetime
import logging

from django.template import RequestContext
from django.http import Http404
from django.shortcuts import render_to_response

from models import Post
from utils import get_archive_posts, valid_month_param

_LOGGER = logging.getLogger('blog.custom')


def tagpage(request, tag):
    """View responsible for showing all posts for given tag.

    Args:
        request -- request
        tag -- tag by which we filter
    """
    posts = Post.objects.filter(tags__name=tag)
    return render_to_response("tagpage.html", {"posts": posts, "tag": tag})

def _render_archive_posts(request, posts):
    """Render archive posts."""
    now = datetime.datetime.now()

    all_posts = Post.objects.filter().order_by('-created')
    archive_posts = get_archive_posts(all_posts)

    _LOGGER.debug("Posts archive dict: %s", str(archive_posts))

    return render_to_response("blog.html", {"posts": posts, "now": now,
                                            "list_events": archive_posts},
                              context_instance=RequestContext(request))

def index(request):
    """Views main blog page.
    """
    posts = Post.objects.filter().order_by('-created')
    return _render_archive_posts(request, posts)

def archive_month(request, year, month):
    """View for showing posts only from given month."""
    if not valid_month_param(month):
        _LOGGER.warn("Invalid argument 'month': %s", month)
        raise Http404
    posts = Post.objects.filter(created__year=year,
                                created__month=month).order_by('-created')
    return _render_archive_posts(request, posts)

def archive_year(request, year):
    """View for showing posts only from given year."""
    posts = Post.objects.filter(created__year=year).order_by('-created')
    return _render_archive_posts(request, posts)

def photos_index(request):
    """View for showing photos index."""
    return render_to_response("photos.html",
                              context_instance=RequestContext(request))

def team_index(request):
    """View for showing team index."""
    return render_to_response("team.html",
                              context_instance=RequestContext(request))

def links_index(request):
    """View for showing links index."""
    return render_to_response("links.html",
                              context_instance=RequestContext(request))

def contact_index(request):
    """View for showing contact index."""
    return render_to_response("contact.html",
                              context_instance=RequestContext(request))
