import time
import os.path

import sys
import xlrd
import numpy as np
import pandas as pd
import sqlite3 as sq

reload(sys)
sys.setdefaultencoding('utf8')


def xls2list(fname):

    data = xlrd.open_workbook(fname + '.xls')
    table = data.sheets()[0]
    nrows = table.nrows # 获取表的行数
    l = ['word', 'level', 'lenovo', 'etyma', 'meanZh', 'meanEn', 'example', 'phonetic', 'test']

    content = []

    for i in range(1, nrows): # 循环逐行打印
        if i == 0: # 跳过第一行
            continue
        row = table.row_values(i)[:len(l)]
        if len(row) > len(l):
            print len(row), row
            sys.exit()
        content.append(row)

    print len(content)
    return content, l

def list2df(para):
    content, l = para
    data = pd.DataFrame(content, columns=l)

    data['selfLenovo'] = ""
    data['level'] = 0
    return data

def gloss2test(data):

    test = {'CET4':'四级', 'CET6':'六级', 'TOFEL':'托福', 
            'GRE':'GRE', 'GRE3000':'GRE-再要你命3000', 
            'GREmagoosh':'GRE-Magoosh'}

    f = file("books.txt", "w")

    for t in test:
        if t == 'CET6':
            subset = data[(data['test'].str.contains(t))&(~data['test'].str.contains('CET4'))]
        else:
            subset = data[(data['test'].str.contains(t))]

        print t, len(subset)
        con  = sq.connect(t.lower() + '.db')
        subset[subset.columns[:-1]].to_sql('word', con)
        con.close()

        m = time.strftime('%Y-%m-%d-%H:%M:%S', time.localtime(os.path.getmtime('gloss.xls')))
        s = "%s http://7xt8es.com1.z0.glb.clouddn.com/naodong/word/%s.db %d(%s更新)" % (test[t], t.lower(), len(subset), m)

        f.write(s)

        f.write('\n')

    f.close()


if __name__ == '__main__':
    gloss2test(list2df(xls2list('gloss3')))
