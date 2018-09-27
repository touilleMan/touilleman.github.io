#!/usr/bin/env python
# -*- coding: utf-8 -*- #
from __future__ import unicode_literals
from os import environ


AUTHOR = 'Emmanuel Leblond'
SITENAME = 'touilleMan.xyz'
SITEURL = ''
TWITTER_USERNAME = 'touilleMan'
GITHUB_URL = 'https://github.com/touilleMan'

TAGLINE = 'Open source & Python lover'
THEME = "pelican-themes/pure-single"
PROFILE_IMG_URL = '/extra/touilleman.jpeg'
# COVER_IMG_URL = ''
WITH_JQUERY = False
WITH_FONT_AWESOME = False
PATH = 'content'
STATIC_PATHS = ['blog', 'extra']
FAVICON_URL = '/extra/touilleman.jpeg'
EXTRA_PATH_METADATA = {
    'extra/_redirects': {'path': '_redirects'},
    'extra/keybase.txt': {'path': 'keybase.txt'},
    'extra/CNAME': {'path': 'CNAME'},
}
ARTICLE_PATHS = ['blog']
ARTICLE_URL = 'blog/{slug}'
ARTICLE_SAVE_AS = 'blog/{slug}.html'
PAGE_URL = '{slug}'
PAGE_SAVE_AS = '{slug}.html'

TIMEZONE = 'Europe/Paris'

DEFAULT_LANG = 'en'

# Feed generation is usually not desired when developing
FEED_ALL_ATOM = None
CATEGORY_FEED_ATOM = None
TRANSLATION_FEED_ATOM = None
AUTHOR_FEED_ATOM = None
AUTHOR_FEED_RSS = None

# Blogroll
LINKS = ()
# LINKS = (('Pelican', 'http://getpelican.com/'),
#          ('Python.org', 'http://python.org/'),
#          ('Jinja2', 'http://jinja.pocoo.org/'),)
MENUITEMS = (
    ('About', '/about'),
    ('Python', '/category/python.html'),
    ('Misc', '/category/misc.html'),)

# Social widget
SOCIAL = (
    ('twitter', 'https://twitter.com/touilleMan'),
    ('github', 'https://github.com/touilleMan'),
    ('rss', '/feeds/all.atom.xml'))

DEFAULT_PAGINATION = 10

# Uncomment following line if you want document-relative URLs when developing
# RELATIVE_URLS = None
