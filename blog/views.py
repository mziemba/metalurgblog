#!/usr/bin/python
# -*- coding: utf-8 -*-

"""Definition of views used by blog app."""

__author__ = "M. Ziemba"
__date__   = "2012-05-16, 23:11"

import logging
from django.template import RequestContext
from django.http import Http404
from django.shortcuts import render_to_response
from django.contrib import messages
from django.contrib.auth import logout
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.comments import Comment
from django.contrib.comments.signals import comment_was_posted

from models import Post, Tournament, Link, Player
from forms import CustomRegistrationForm
from utils import valid_month_param, get_extra_context

_LOGGER = logging.getLogger('blog.custom')


# USERS

def logout_view(request):
    logout(request)
    return posts_index(request)

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


# POSTS

def posts_index(request):
    """Views main blog page."""
    posts = Post.objects.filter().order_by('-created')[:10]
    return _render_archive_posts(request, posts)

def posts_single(request, post_id):
    """View for showing single blog post."""
    extra_context = get_extra_context()
    post = Post.objects.get(pk=post_id)
    extra_context['post'] = post

    return render_to_response("post.html", extra_context,
                              context_instance=RequestContext(request))


# COMMENTS

def comment_messages(sender, comment, request, **kwargs):
    if request.user.is_authenticated():
        messages.add_message(
            request,
            messages.SUCCESS,
            ('Komentarz został dodany')
        )

comment_was_posted.connect(comment_messages, sender=Comment)


# TAGS

def tagpage(request, tag):
    """View responsible for showing all posts for given tag."""
    extra_context = get_extra_context()
    posts = Post.objects.filter(tags__name=tag)
    extra_context['posts'] = posts
    extra_context['tag'] = tag
    return render_to_response("tagpage.html", extra_context,
                              context_instance=RequestContext(request))


# ARCHIVES

def _render_archive_posts(request, posts):
    """Render archive posts."""
    extra_context = get_extra_context()
    extra_context['posts'] = posts
    return render_to_response("blog.html", extra_context,
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


# GALLERY

def photos_index(request):
    """View for showing photos index."""
    extra_context = get_extra_context()
    return render_to_response("photos.html", extra_context,
                              context_instance=RequestContext(request))


# FIXTURES

def tournaments_list(request):
    """View for showing tournaments index."""
    extra_context = get_extra_context()
    tournaments = Tournament.objects.filter().order_by('-created')
    extra_context['tournaments'] = tournaments
    return render_to_response("fixtures/list.html", extra_context,
                              context_instance=RequestContext(request))

def tournament(request, tournament_id):
    """View for showing fixtures for a single tournament."""
    extra_context = get_extra_context()
    tournament = Tournament.objects.get(pk=tournament_id)
    extra_context['tournament'] = tournament
    return render_to_response("fixtures/single.html", extra_context,
                              context_instance=RequestContext(request))


# TEAM

def team_index(request):
    """View for showing team index."""
    extra_context = get_extra_context()
    players = Player.objects.filter().order_by('-number')
    extra_context['players'] = players
    return render_to_response("team.html", extra_context,
                              context_instance=RequestContext(request))

# OTHER

def achivements(request):
    """View for showing achivements."""
    extra_context = get_extra_context()
    return render_to_response("achivements.html", extra_context,
                              context_instance=RequestContext(request))

def links_index(request):
    """View for showing links index."""
    extra_context = get_extra_context()
    links = Link.objects.all()
    extra_context['links'] = links
    return render_to_response("other/links.html", extra_context,
                              context_instance=RequestContext(request))

# ERROR

def server_error(request):
    return render_to_response("error/500.html",
                              context_instance=RequestContext(request))

def page_not_found(request):
    extra_context = get_extra_context()
    return render_to_response("error/404.html", extra_context,
                              context_instance=RequestContext(request))
