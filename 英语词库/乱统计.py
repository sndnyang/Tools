import sys
import xlrd
import numpy as np
import pandas as pd

data = xlrd.open_workbook(sys.argv[1])
table = data.sheets()[0]
nrows = table.nrows # 获取表的行数
l = ['word', 'level', 'lenovo', 'etyma', 'meanZh', 'meanEn', 'example']

content = []

for i in range(2, nrows): # 循环逐行打印
    if i == 0: # 跳过第一行
        continue
    row = table.row_values(i)[:len(l)]
    if len(row) > 7:
        print len(row), row
        sys.exit()
    content.append(row)

data = pd.DataFrame(content, columns=l)

tmp = data[data['level'] <= 0.2]
print len(tmp)

a = pd.Series([e[0] for e in tmp['word']])

t = pd.DataFrame({'c': a})

t['a'] = 1

print t.groupby('c').count().sort_values('a')

#print data[:3]

#tmp = data[data['lenovo'] == ""]
tmp = data[data['level'] <= 2.2]
#tmp = tmp[tmp['lenovo'] == ""]

print len(tmp)

a = pd.Series([e[0] for e in tmp['word']])

t = pd.DataFrame({'c': a})

t['a'] = 1

print t.groupby('c').count().sort_values('a')

