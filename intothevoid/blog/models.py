#!/usr/bin/python
# -*- coding: utf-8 -*-

"""Definition of models.
"""

__author__ = "M. Ziemba"
__date__   = "2012-05-16, 23:05"

from django.db import models
from taggit.managers import TaggableManager


class Post(models.Model):
    """Class representing a single post.

    Fields:
        title -- post title
        body -- post body text
        created -- creation date
        tags -- list of tags attached to post
    """

    title = models.CharField(max_length=100)
    body = models.TextField()
    created = models.DateTimeField()
    tags = TaggableManager()

    def __unicode__(self):
        return self.title
