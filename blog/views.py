# -*- coding: utf-8 -*-

"""Definition of views used by blog app."""

__author__ = "M. Ziemba"
__date__   = "2012-05-16, 23:11"

import datetime
import logging
from django.template import RequestContext
from django.http import Http404, HttpResponseRedirect
from django.shortcuts import render_to_response
from django.contrib import messages
from django.contrib.auth import logout
from django.contrib.auth.forms import AuthenticationForm

from models import Post, Game, Link
from forms import CustomRegistrationForm
from utils import get_archive_posts, valid_month_param, get_extra_context

_LOGGER = logging.getLogger('blog.custom')


def logout_view(request):
    logout(request)
    return HttpResponseRedirect('/blog')

def register(request):
    """User registration view."""
    extra_context = get_extra_context()
    if request.method == 'POST':
        user_form = CustomRegistrationForm(request.POST)

        if user_form.is_valid():
            user_form.save()
            messages.info(request, 'Dodano nowego użytkownika')
            login_form = AuthenticationForm()
            extra_context['form'] = login_form
            return render_to_response("login.html", extra_context,
                                      context_instance=RequestContext(request))
    else:
        user_form = CustomRegistrationForm()

    extra_context['form'] = user_form
    return render_to_response("register.html", extra_context,
                              context_instance=RequestContext(request))

def tagpage(request, tag):
    """View responsible for showing all posts for given tag.

    Args:
        request: request
        tag: tag by which we filter
    """
    posts = Post.objects.filter(tags__name=tag)
    return render_to_response("tagpage.html", {"posts": posts, "tag": tag},
                              context_instance=RequestContext(request))

def _render_archive_posts(request, posts):
    """Render archive posts."""
    now = datetime.datetime.now()

    all_posts = Post.objects.filter().order_by('-created')
    archive_posts = get_archive_posts(all_posts)

    recent_games = Game.objects.filter().order_by('-date')[:5]

    return render_to_response("blog.html", {"posts": posts, "now": now,
                                            "list_events": archive_posts,
                                            "recent_games": recent_games},
                              context_instance=RequestContext(request))

def _render_default(request, page, obj=None):
    """Default render."""
    now = datetime.datetime.now()

    all_posts = Post.objects.filter().order_by('-created')
    archive_posts = get_archive_posts(all_posts)

    recent_games = Game.objects.filter().order_by('-date')[:5]

    injected = {"now": now, "list_events": archive_posts,
                "recent_games": recent_games}
    if obj is not None:
        injected['obj'] = obj

    return render_to_response(page, injected,
                              context_instance=RequestContext(request))

def posts_index(request):
    """Views main blog page.
    """
    posts = Post.objects.filter().order_by('-created')
    return _render_archive_posts(request, posts)

def posts_single(request, post_id):
    """View for showing single blog post."""
    post = Post.objects.get(pk=post_id)
    now = datetime.datetime.now()

    all_posts = Post.objects.filter().order_by('-created')
    archive_posts = get_archive_posts(all_posts)

    recent_games = Game.objects.filter().order_by('-date')[:5]

    return render_to_response("post.html", {"post": post,
                                     "now": now,
                                     "list_events": archive_posts,
                                     "recent_games": recent_games},
                              context_instance=RequestContext(request))

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
    return _render_default(request, 'photos.html')

def team_index(request):
    """View for showing team index."""
    return _render_default(request, 'team.html')

def links_index(request):
    """View for showing links index."""
    links = Link.objects.all()
    return _render_default(request, 'links.html', obj=links)

def contact_index(request):
    """View for showing contact index."""
    return _render_default(request, 'contact.html')

def handler404(request):
    """View for 404 Not Found errors"""
    return render_to_response('error/404.html',
                              context_instance=RequestContext(request))
