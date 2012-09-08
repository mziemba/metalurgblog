# -*- coding: utf-8 -*-

"""Utilities for blog application. """

__author__ = "M. Ziemba"
__date__ = "2012-06-11, 23:31"

import datetime

from models import Post
from models import Game


def get_extra_context():
    now = datetime.datetime.now()

    all_posts = Post.objects.filter().order_by('-created')
    archive_posts = get_archive_posts(all_posts)

    recent_games = Game.objects.filter().order_by('-date')[:5]
    return {"now": now,
            "list_events": archive_posts,
            "recent_games": recent_games}

def get_archive_posts(posts):
    """Get dict with posts archive grouped by years/months.

    Returns:
        dict
    """

    #create a dict with the years and months:posts
    event_dict = {}
    for i in range(posts[0].created.year, posts[len(posts)-1].created.year-1, -1):
        event_dict[i] = {}
        for month in range(1, 13):
            event_dict[i][month] = []
    for event in posts:
        event_dict[event.created.year][event.created.month].append(event)

    #this is necessary for the years to be sorted
    event_sorted_keys = list(reversed(sorted(event_dict.keys())))
    list_events = []
    for key in event_sorted_keys:
        adict = {key:event_dict[key]}
        list_events.append(adict)

    return list_events

def valid_month_param(month):
    """Checks if given month is an int of value 1-12."""
    try:
        month = int(month)
    except:
        return False
    if month < 1 or month > 12:
        return False
    return True
