#!/usr/bin/python
# -*- coding: utf-8 -*-

"""Admin bindings for blog application."""

__author__ = "M. Ziemba"
__date__ = "2012-05-16, 23:04"

from django.contrib import admin
from blog.models import (Post, Tournament, Fixture, Link, Player, Position,
    Album, Photo)

admin.site.register(Post)
admin.site.register(Tournament)
admin.site.register(Fixture)
admin.site.register(Link)
admin.site.register(Player)
admin.site.register(Position)
admin.site.register(Album)
admin.site.register(Photo)
