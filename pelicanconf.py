#!/usr/bin/env python
# -*- coding: utf-8 -*- #
from __future__ import unicode_literals

AUTHOR = u'Ivan FF'
SITENAME = u'Ivan FF'
SITEURL = 'http://127.0.0.1:8080'

# URLS
TAGS_URL = 'tags'
CATEGORIES_URL = 'categories'

PATH = 'content'

TIMEZONE = 'America/Los_Angeles'

DEFAULT_LANG = u'en'

# Feed generation is usually not desired when developing
FEED_ALL_ATOM = None
CATEGORY_FEED_ATOM = None
TRANSLATION_FEED_ATOM = None
AUTHOR_FEED_ATOM = None
AUTHOR_FEED_RSS = None

# Blogroll
LINKS = (('Pelican', 'http://getpelican.com/'),
         ('Python.org', 'http://python.org/'),
         ('Jinja2', 'http://jinja.pocoo.org/'),
         ('You can modify those links in your config file', '#'),)

# Social widget
SOCIAL = (('You can add links in your config file', '#'),
          ('Another social link', '#'),)

DEFAULT_PAGINATION = 5
DEFAULT_DATE = 'fs'

# Uncomment following line if you want document-relative URLs when developing
#RELATIVE_URLS = True

# Theme
THEME = "themes/bootstrap3"
BOOTSTRAP_THEME = 'paper'
DISPLAY_BREADCRUMBS = True
DISPLAY_CATEGORY_IN_BREADCRUMBS = True
DISPLAY_ARTICLE_INFO_ON_INDEX = True
SHOW_ARTICLE_AUTHOR = True
DISPLAY_CATEGORIES_ON_MENU = False
DISPLAY_PAGES_ON_MENU = False
DISPLAY_RECENT_POSTS_ON_SIDEBAR = True
DISPLAY_CATEGORIES_ON_SIDEBAR = True
