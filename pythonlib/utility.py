# coding: utf-8

def printDeep(item, deep):
    if isinstance(item, (str, bool, int, float)):
        print ' '*deep, item
    elif isinstance(item, (list, tuple)):
        print ' '*deep, 'a list'
        for e in item:
            if isinstance(e, (str, bool, int, float, unicode)):
                print ' '*(deep+4), e
            else:
                printDeep(e, deep+4)
    elif isinstance(item, dict):
        print ' '*deep, 'a dict'
        for e in item:
            if not item[e]:
                continue
            if not isinstance(item[e], (str, bool, int, float)):
                print ' '*(deep+4), e,
                printDeep(item[e], deep+4)
            else:
                print ' '*(deep+4), e, ':', item[e]
