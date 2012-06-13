#!/usr/bin/python
# -*- coding: utf-8 -*-

"""Admin bindings for blog application.
"""

__author__ = "M. Ziemba"
__date__   = "2012-05-16, 23:04"

from django.contrib import admin
from models import User, Post, Game, Link

admin.site.register(User)
admin.site.register(Post)
admin.site.register(Game)
admin.site.register(Link)
