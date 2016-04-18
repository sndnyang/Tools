#!/usr/bin/env python
# -*- coding: utf-8 -*- #
from __future__ import unicode_literals

import sys

if sys.getdefaultencoding() != 'utf8':
    reload(sys)
    sys.setdefaultencoding('utf8')

            
AUTHOR = u'sndnyang'
SITENAME = u'\u61d2\u9f99\u8c37'
SITEURL = ''

MARKUP=('rst', 'md', 'markdown')
PATH = 'content'

TIMEZONE = 'Asia/Shanghai'

DEFAULT_LANG = u'zh'

# Feed generation is usually not desired when developing
FEED_ALL_ATOM = None
CATEGORY_FEED_ATOM = None
TRANSLATION_FEED_ATOM = None
AUTHOR_FEED_ATOM = None
AUTHOR_FEED_RSS = None

THEME = 'G:\software\open_source\pelican-elegant'
PLUGIN_PATHS = ['G:\software\open_source\pelican-plugins']
PLUGINS = ['sitemap', 'extract_toc', 'tipue_search', 'ipynb.liquid', "render_math"]
MD_EXTENSIONS = ['codehilite(css_class=highlight)', 'extra', 'headerid', 'toc', 'problem']
DIRECT_TEMPLATES = (('index', 'tags', 'categories','archives', 'search', '404'))
STATIC_PATHS = ['theme/images', 'images']
TAG_SAVE_AS = ''
CATEGORY_SAVE_AS = ''
AUTHOR_SAVE_AS = ''

# Blogroll
LINKS = (('Pelican', 'http://getpelican.com/'),
         ('Python.org', 'http://python.org/'),
         ('Jinja2', 'http://jinja.pocoo.org/'),
         ('You can modify those links in your config file', '#'),)

# Social widget
SOCIAL = (('You can add links in your config file', '#'),
          ('Another social link', '#'),)

LANDING_PAGE_ABOUT = {'title': '卧龙凤雏，得一可安天下。', 
        "details": '''I'm sndnyang, <a href="https://github.com/sndnyang">
        sndnyang</a> at github and  <a href="http://blog.csdn.net/sndnyangd">
        sndnyangd</a> at csdn.<br>
        有理想，没动作的卧龙。
        '''}
DEFAULT_PAGINATION = 10

PROJECTS = [{
    'name': 'gpa 计算器',
    'url': 'gpa_calculator.html',
    'description': '就是一个计算器'},
    {'name': 'algorithm vis study',
    'url': 'ds_alg_code.html',
    'description': 'a project use ideas from tryregex, elegatorsaga, based on'
    'vis.js to learn algorithm'},
    {'name': 'brain learn lab',
    'url': 'http://zhimind.com',
    'description': 'a project I hope to push the education field forward! Make'
    'a difference by all means'}]

disqus_identifier = "sndnyang"   

RECENT_ARTICLES_COUNT = 15
# Uncomment following line if you want document-relative URLs when developing
#RELATIVE_URLS = True
