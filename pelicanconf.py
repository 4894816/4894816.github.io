#!/usr/bin/env python
# -*- coding: utf-8 -*- #
from __future__ import unicode_literals

AUTHOR = u'Dash'
SITENAME = u"Dash's Qzone"
SITEURL = ''

TIMEZONE = 'Europe/Paris'

DEFAULT_LANG = u'en'

# Feed generation is usually not desired when developing
FEED_ALL_ATOM = None
CATEGORY_FEED_ATOM = None
TRANSLATION_FEED_ATOM = None

# Blogroll
LINKS =  (('4894816', 'http://4894816.qzone.qq.com/'), 
          ('Pelican', 'http://getpelican.com/'),
          ('Python.org', 'http://python.org/'),
          ('Jinja2', 'http://jinja.pocoo.org/'),)
          #('You can modify those links in your config file', '#'),)

# Social widget
SOCIAL = (
         #('You can add links in your config file', '#'),
          ('Another social link', '#'),)

DEFAULT_PAGINATION = 10

# Use theme for our own
# THEME = "./pelican-themes/waterspill-en"
# THEME = "/home/qzone/pelican-themes/bootstrap"
THEME = "/home/qzone/pelican-themes/bluegrasshopper"  # Very Good
# THEME = "/home/qzone/pelican-themes/sundown"   # Very Clear
# THEME = "/home/qzone/pelican-themes/pelipress"
# THEME = "/home/qzone/pelican-themes/plumage" # Not so good
# THEME = "/home/qzone/pelican-themes/fresh"

#######################################################
# Add disqus for guests to leave comments
#######################################################
DISQUS_SITENAME = "4894816githubio"
DISQUS_SHORTNAME = "4894816githubio"

# Uncomment following line if you want document-relative URLs when developing
#RELATIVE_URLS = True
