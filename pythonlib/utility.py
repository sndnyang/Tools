# coding: utf-8
import sys
if sys.version_info >= (3,0):
    print_obj = (str, bool, int, float)
    str_obj = str
else:
    print_obj = (str, bool, int, float, unicode)
    str_obj = (str, unicode)

def printDeep(item, deep):
    if isinstance(item, print_obj):
        print(' '*deep, item)
    elif isinstance(item, (list, tuple)):
        print(' '*deep, 'a list: ')
        for e in item:
            if isinstance(e, print_obj):
                print(' '*(deep+4), e)
            else:
                printDeep(e, deep+4)
    elif isinstance(item, dict):
        print(' '*deep, 'a dict, keys: ', item.keys())
        for e in item:
            if not isinstance(item[e], print_obj):
                print(' '*(deep+4), e,)
                printDeep(item[e], deep+4)
            else:
                print(' '*(deep+4), e, ':', item[e])


def format_url(href):
    if href[0] == '/':
        url = domain + href
    elif href.startswith('http'):
        url = href
    elif href.startswith('//'):
        url = 'http:' + href
    elif href.find(university_name) > -1:
        url = 'http://' + href
    else:
        url = "Error!!!!!! at", href
    return url


def replace_html(s):
    s = s.replace('&quot;','"')
    s = s.replace('&amp;','&')
    s = s.replace('&lt;','<')
    s = s.replace('&gt;','>')
    s = s.replace('&nbsp;',' ')
    s = s.replace('\xc2\xa0','')
    return s