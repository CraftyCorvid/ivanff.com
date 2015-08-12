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
         ('Jinja2', 'http://jinja.pocoo.org/'))

# Social widget
SOCIAL = (('Facebook', 'https://www.facebook.com/Hideaki02'),
          ('Google+', 'https://google.com/+IvanFerrariFossa'),
          ('Linkedin', 'https://www.linkedin.com/pub/ivan-fossa-ferrari/28/154/23'),
          ('Twitter', 'https://twitter.com/hideaki042'),)
          
# Share Buttons (Sharrif)
SHARIFF = True
SHARIFF_SERVICES = '[&quot;facebook&quot;,&quot;googleplus&quot;,&quot;twitter&quot;]'
SHARIFF_LANG = 'en'
SHARIFF_THEME = 'grey'
TWITTER_USERNAME = 'hideaki02'
SHARIFF_TWITTER_VIA = True
          
# Paths
STATIC_PATHS = ['extra', 'blog', 'pages']
EXTRA_PATH_METADATA = {'extra/CNAME': {'path': 'CNAME'},
                       'extra/custom.css': {'path': 'static/custom.css'},}
ARTICLE_PATHS = ['blog']
ARTICLE_SAVE_AS = 'blog/{date:%Y}/{date:%b}/{slug}.html'
ARTICLE_URL = 'blog/{date:%Y}/{date:%b}/{slug}.html'

# Post Settings
DEFAULT_PAGINATION = 5
DEFAULT_DATE = 'fs'

# Uncomment following line if you want document-relative URLs when developing
#RELATIVE_URLS = True

# Theme
THEME = "themes/bootstrap3"
CUSTOM_CSS = 'static/custom.css'
BOOTSTRAP_THEME = 'darkly'
DISPLAY_ARTICLE_INFO_ON_INDEX = True
DISPLAY_CATEGORIES_ON_MENU = False
GITHUB_USER = 'ivan0xff'
GITHUB_SHOW_USER_LINK = True
