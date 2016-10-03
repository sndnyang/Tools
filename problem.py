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
from . import Extension
from ..preprocessors import Preprocessor
from ..inlinepatterns import Pattern
from ..util import etree

import re
import md5

# 自定义的 problem 格式
# 格式定义（一行）：
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
        md.inlinePatterns.add('problem', ProblemPattern(BASE_RE), '>not_strong')


class ProblemPattern(Pattern):
    """ Problem inline pattern. """

    def __init__(self, pattern):
        super(ProblemPattern, self).__init__(pattern)
        self.quiz_count = 0

    def handleMatch(self, m):
        sterm = m.group()

        pattern = '{%([^|]*)\|([^@]*)@([^#]*)'
        parts = re.findall(pattern, sterm)[0]

        div = etree.Element('div')
        question = parts[1]
        br = etree.Element('br')
        submit = etree.Element('button')
        submit.text = 'submit'
        self.quiz_count += 1
        submit.set('onclick', "checkQuiz(this, %d)"%self.quiz_count)

        if parts[0] == "radio" or parts[0] == "checkbox":
            etype = parts[0]
            qparts = question.split('&')
            p = etree.Element('p')
            p.text = qparts[0]
            div.append(p)
            template = '<input type="%s" class="quiz" name="quiz" value="%s">'\
                    +'</input>'
            for v in qparts[1:]:
                ele = etree.fromstring(template % (etype, v))
                label = etree.Element('b')
                label.text = v
                div.append(ele)
                div.append(label)
                div.append(br)

            div.append(submit)
            div.append(br)

        elif parts[0] == "text":
            blank = '<input type="text" class="quiz"/>'
            question = question.replace('_', blank)
            div.append(etree.fromstring('<p>'+question+'</p>'))
            div.append(br)
            div.append(submit)
            div.append(br)

        if parts[0] == "formula":
            blank = '<input type="text" class="quiz formula" '
            blank += 'onchange="Preview.Update(this)"/>\n' 
            blank += '<div id="MathPreview"></div>\n'

            question = question.replace('_', blank)

            div.append(etree.fromstring('<p>'+question+'</p>'))
            div.append(submit)
            div.append(br)
        else:
            tmp = md5.new()
            tmp.update(parts[2])
            encry = tmp.hexdigest()
            template = '<input type="hidden" class="answers" value="%s"></input>'
            ele = template % encry
            div.append(etree.fromstring(ele))

        comment_pos = sterm.find('#')
        if comment_pos:
            comments = re.findall('#([^%}]*)', sterm)
            if comments:
                comments = comments[0]
                template = '<input type="hidden" class="comments"></input>'
                comment = etree.fromstring(template)
                comment.set('value', comments)
                div.append(comment)

        div.append(br)

        return div


def makeExtension(*args, **kwargs):
    return ProblemExtension(*args, **kwargs)
