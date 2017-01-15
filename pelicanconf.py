#!/usr/bin/env python
# -*- coding: utf-8 -*- #
from __future__ import unicode_literals

import sys

if sys.getdefaultencoding() != 'utf8':
    reload(sys)
    sys.setdefaultencoding('utf8')

            
AUTHOR = u'sndnyang'
SITENAME = u'\u61d2\u9f99\u8c37'
DISQUS_SITENAME = 'sndnyang'
SITEURL = 'http://sndnyang.github.io'

MARKUP=('rst', 'md', 'markdown', 'dmd')
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
        "details": '''I'm sndnyang, <a href="https://sndnyang.github.io">
        sndnyang</a> at github <br>  <a href="http://blog.csdn.net/sndnyangd">
        sndnyangd</a> at csdn<br> <a href="https://www.zhihu.com/people/yang-xiu-long">
        杨成</a> at 知乎<br> <a href="http://weibo.com/u/2405149384">sndnyang</a>
        at 微博。<br>
        有理想有但很难动作的懒龙。先战教育(启发、交互式教育 zhimind.com），再搞医疗（不会），学习自然语言处理和人工智能、机器学习<br>
        ambitious but lazy,  first goal is the education(heuristic, interactive education technology www.zhimind.com), then health care(have no idea now)<br>
        doing these by learning and applying natural language processing and artificial intelligence and machine learning.
        '''}

DEFAULT_PAGINATION = 10

PROJECTS = [{'name': '知维图',
    'url': 'http://zhimind.com',
    'description': 'zhimind a project I hope to push the education field forward! Make'
    'a difference by all means 知维图 智能交互教学实验'},
    {'name': '格物学习-费曼技巧(实验)',
    'url': 'http://www.zhimind.com/gewu.html',
    'description': 'gewu a project I hope to push the education field forward too! Let '
    'us learn using Feynman Technique 格物学习助手--费曼技巧 (beta)'},
    {'name': '脑洞单词(实验)',
    'url': 'http://www.zhimind.com/reciteWord.html',
    'description': '自己编写联想记忆法，找词根词缀等方式来记忆单词，联想记忆法效率会高一些'},
    {'name': '幻灯片',
    'url': 'slides_set.html',
    'description': '制作的文本幻灯片集合， 应该多数是读论文的笔记'},
    {
    'name': 'gpa 计算器',
    'url': 'gpa_calculator.html',
    'description': '就是一个计算器'},
    {'name': 'algorithm vis study',
    'url': 'ds_alg_code.html',
    'description': 'a project use ideas from tryregex, elegatorsaga, based on'
    'vis.js to learn algorithm'},
    {'name': 'zhimind编辑器',
    'url': '/zhimindEditor.html',
    'description': '基于markdown-it及其插件的markdown在线编辑，正好用于zhimind教程和练习的展示和编辑'},
    {'name': '其他',
    'url': '/other.html',
    'description': '之前不小心把markdown笔记全部删了， 只剩html， ' 
        '有些文件不想重新制作'}]

#disqus_identifier = "sndnyang.github.io"   

RECENT_ARTICLES_COUNT = 15
COMMENTS_INTRO  = "this man is lazy, nothing left"
# Uncomment following line if you want document-relative URLs when developing
#RELATIVE_URLS = True
