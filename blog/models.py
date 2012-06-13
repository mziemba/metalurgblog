#!/usr/bin/python
# -*- coding: utf-8 -*-

"""Definition of models."""

__author__ = "M. Ziemba"
__date__   = "2012-05-16, 23:05"

from django.db import models
from taggit.managers import TaggableManager


class User(models.Model):
    """Class representing a single user.

    Fields:
        login: user login
    """
    login = models.CharField(max_length=64)

    def __unicode__(self):
        return self.login


class Post(models.Model):
    """Class representing a single post.

    Fields:
        title: post title
        body: post body text
        image_uri: uri of image associated with post
        created: creation date
        tags: list of tags attached to post
        owner: creator of post
    """

    title = models.CharField(max_length=100)
    body = models.TextField()
    image_uri = models.CharField(max_length=50)
    created = models.DateTimeField()
    tags = TaggableManager()
    owner = models.ForeignKey(User)

    def __unicode__(self):
        return self.title

class Game(models.Model):
    """Class representing a single game.

    Fields:
    """
    date = models.DateTimeField()
    home = models.CharField(max_length=100)
    away = models.CharField(max_length=100)
    home_score = models.IntegerField()
    away_score = models.IntegerField()

    def __unicode__(self):
        return "%s - %s" % (self.home, self.away)

class Link(models.Model):
    """Class representing a single http link."""

    url = models.CharField(max_length=128)
    description = models.CharField(max_length=255)

    def __unicode__(self):
        return self.url
