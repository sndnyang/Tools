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
        print(' '*deep + unicode(item))
    elif isinstance(item, (list, tuple)):
        print(' '*deep +'a list: ')
        for e in item:
            if isinstance(e, print_obj):
                print(' '*(deep+4) + unicode(e))
            else:
                printDeep(e, deep+4)
    elif isinstance(item, dict):
        print(' '*deep + 'a dict, keys: ' + (item.keys()))
        for e in item:
            if not isinstance(item[e], print_obj):
                print(' '*(deep+4) + e,)
                printDeep(item[e], deep+4)
            else:
                print(' '*(deep+4) + unicode(e) + ' : ' + unicode(item[e]))


def format_url(href, domain, index=''):
    if href.startswith('http'):
        full_url = href
    elif href.startswith('//'):
        full_url = 'http:' + href
    elif href[0] == '/' and (len(href) == 1 or href[1] != '/'):
        full_url = domain + href
    elif href.find(domain) > -1:
        full_url = 'http://' + href
    elif index:
        full_url = index + href if index[-1] == '/' else index + '/' + href
    else:
        full_url = domain + '/' + href
    return full_url


def replace_html(s):
    s = s.replace('&quot;','"')
    s = s.replace('&amp;','&')
    s = s.replace('&lt;','<')
    s = s.replace('&gt;','>')
    s = s.replace('&nbsp;',' ')
    s = s.replace('\xc2\xa0','')
    return s


def contain_keys(href, keys, is_name=False, return_obj=False):
    """

    """
    if not href or not keys:
        return False
    words = "(%s)" % '|'.join(e for e in keys)
    if is_name:
        r = re.search('%s' % words, href, re.I)
        if r:
            if return_obj:
                return r
            return True
    r = re.search(r'\b%s\b' % words, href, re.I)
    if r:
        if return_obj:
            return r
        return True
    r = re.search(r'_?%s_?' % words, href, re.I)
    if r:
        if return_obj:
            return r
        return True
    return False