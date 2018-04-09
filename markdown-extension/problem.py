# -*- coding:utf-8 -*-
"""
Problem Extension for Python-Markdown
============================================

Adds Problem syntax. Inspired by xxx

See 
for documentation.

"""

from __future__ import absolute_import
from __future__ import unicode_literals

import sys
import traceback
from . import Extension
from ..preprocessors import Preprocessor
from ..inlinepatterns import Pattern

import re
import md5

from lxml import etree

from .qa_parser import *

# 自定义的 problem 格式
# 格式定义：
#    {% type
#       |可填题干 &
#       &a&b&c 选择题的选项 
#       @a@b答案，多选题和多空格的答案用@分开 
#       #提示1#提示2]
#    %}
#
# 主要类型， 及示例
# {%radio|请选择&a&b&c&d@d#随便%} 单选
# {%checkbox|请选择&a&b&c&d@d#随便%} 多选
# {%text|请填空:_是有意义的@教育#随便%}  填空
# {%formula|请填空:公式_@(1+6*x^3*x^2)/(2+5*x^4)+9#随便%}  填空（单空公式）
#

BASE_RE = r'^{%(\w*|[^%{}@]*@[^%}]*)%?}'


class ProblemExtension(Extension):
    """ Problem Extension for Python-Markdown. """

    def extendMarkdown(self, md, md_globals):
        """ Insert ProblemPreprocessor before ReferencePreprocessor. """
        # md.inlinePatterns.add('problem', ProblemPattern(BASE_RE), '>not_strong')
        problemer = ProblemProcessor(md)
        md.registerExtension(self)
        md.preprocessors.add('problem', problemer,
                             ">normalize_whitespace")



def renderQuestion(s, quiz_count):
    p = re.compile('\s+')
    s = re.sub(p, '', s, re.M)
    quiz_type = re.search('^{%(\w+)|', s, re.M).group(1)

    # div = $('<div class="process"></div>');
    # feedback = $('<div class="hidden"></div>');
    # response = $('<div class="math-container"></div>'),
    # submit = $('<button class="btn btn-info">提交验证</button>');

    div = etree.Element('div')
    div.set('class', 'process')

    cdiv = etree.Element('div')
    cdiv.set('class', 'math-container')

    span = etree.Element('span')

    question = s[s.find('|')+1:s.find('@')].strip()

    submit = etree.Element('button')
    submit.text = 'submit'
    submit.set('onclick', "checkQuiz(this, %d)"%quiz_count)

    if quiz_type == "radio" or quiz_type == "checkbox":
        etype = quiz_type
        qparts = question.split('&')
        p = etree.Element('p')
        p.text = qparts[0]
        span.append(p)
        template = '<input type="%s" class="quiz" name="quiz" value="%s">%s'\
                +'</input>'
        for v in qparts[1:]:
            ele = etree.fromstring(template % (etype, v, v))
            span.append(ele)
            span.append(etree.Element('br'))

        div.append(span)
        div.append(etree.Element('br'))

    elif quiz_type == "text":
        blank = '<input type="text" class="quiz"/>'
        question = question.replace('_', blank)
        span.append(etree.fromstring('<p>'+question+'</p>'))
        div.append(span)
        div.append(etree.Element('br'))

    if quiz_type == "formula":
        blank = '<input type="text" class="quiz formula" '
        blank += 'onchange="Preview.Update(this)"/>\n' 
        blank += '<div id="MathPreview">预览:</div>\n'

        question = question.replace('_', blank)

        span.append(etree.fromstring('<p>'+question+'</p>'))
        div.append(span)
        div.append(etree.Element('br'))

    answers = s[s.find('@')+1:s.find('#')]
    try:
        t = etree.fromstring('<input type="hidden" class="answers"/>')
        t.set("value", answers)
        div.append(t)
    except:
        sys.stderr.write(ele + '    ' + answers)
        print answers, ele
        print traceback.print_exc()

    comments = finite_status_machine(s[s.find('#')+1:], '#')
    if comments:
        template = '<input type="hidden" class="comments"></input>'
        comment = etree.fromstring(template)
        comment.set('value', '#'.join(comments))
        div.append(comment)

    div.append(submit)
    div.append(etree.Element('br'))

    # print etree.tostring(div, encoding='utf8')
    return div


class ProblemProcessor(Preprocessor):
    """ parse multiple line problems"""
    def run(self, lines):
        """ find code blocks problems"""
        content = "\n".join(lines)

        start = content.find("{%")
        lists = []
        while start >= 0 and start < len(content):
            end = find_right_next(content, start, 0, '\n')
            lists.append(content[start:end])
            start = content.find("{%", end)

        c = 0
        for s in lists:
            html = renderQuestion(s, c)
            c += 1
            content = content.replace(s, etree.tostring(html, encoding='utf-8'))
       
        return content.split("\n")


def makeExtension(*args, **kwargs):
    return ProblemExtension(*args, **kwargs)
