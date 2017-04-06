#!/usr/bin/env python
# -*- coding: utf-8 -*- #
from __future__ import unicode_literals
from os import environ


AUTHOR = 'Emmanuel Leblond'
SITENAME = 'touilleMan.xyz'
SITEURL = 'http://touilleman.xyz'
GOOGLE_ANALYTICS = 'UA-42073732-2'
TWITTER_USERNAME = 'touilleMan'
DISQUS_SITENAME = 'touilleman'
GITHUB_URL = 'https://github.com/touilleMan'

PATH = 'content'
STATIC_PATHS = ['blog', 'extra']
EXTRA_PATH_METADATA = {
    'extra/_redirects': {'path': '_redirects'},
    'extra/keybase.txt': {'path': 'keybase.txt'},
    'extra/favicon.ico': {'path': 'favicon.ico'}
}
ARTICLE_PATHS = ['blog']

TIMEZONE = 'Europe/Paris'

DEFAULT_LANG = 'en'

# Feed generation is usually not desired when developing
# FEED_ALL_ATOM = None
# CATEGORY_FEED_ATOM = None
TRANSLATION_FEED_ATOM = None
AUTHOR_FEED_ATOM = None
AUTHOR_FEED_RSS = None

# Blogroll
LINKS = ()
# LINKS = (('Pelican', 'http://getpelican.com/'),
#          ('Python.org', 'http://python.org/'),
#          ('Jinja2', 'http://jinja.pocoo.org/'),)

# Social widget
SOCIAL = (('twitter', 'https://twitter.com/touilleMan'),
          ('github', 'https://github.com/touilleMan'),)

DEFAULT_PAGINATION = 10

# Uncomment following line if you want document-relative URLs when developing
RELATIVE_URLS = 'RELATIVE_URLS' in environ
