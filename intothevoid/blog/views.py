#!/usr/bin/python
# -*- coding: utf-8 -*-

"""Definition of views used by app.
"""

__author__ = "M. Ziemba"
__date__   = "2012-05-16, 23:11"

from models import Post
from django.shortcuts import render_to_response

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
