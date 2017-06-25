# coding: utf-8

import sys
reload(sys)
sys.setdefaultencoding('utf8')

import re
import requests as req
from bs4 import BeautifulSoup as bs

import json
import time
from lxml import etree

college_json = open('college.json')
college_set = json.load(college_json)

def extract_info(href):
    college_page_url = 'https://www.applysquare.com' + href
    college_con = req.get(college_page_url)
    selector = etree.HTML(college_con.text)
    cn = selector.xpath("//a[@class='sp-right']/text()")[0].strip()
    en = selector.xpath("//p[@class='ellipsis']/text()")[0].strip().lower().replace(',', ' -')
    print(en)
    ranks = selector.xpath("//h1[@class='ranking-number pull-left rounded']/text()")
    ranks_item = selector.xpath("//h2[@class='ranking-name ellipsis']/text()")
    rank_dict = dict(zip(ranks_item, ranks))
    rank_dict['cn'] = cn
    for c in college_set:
        if c['name'].lower().find(en) > -1:
            c.update(rank_dict)       
            return False
    rank_dict['name'] = en
    college_set.append(rank_dict)
    return True

tl = 'https://www.applysquare.com/ranking-cn/?country=us&page=%d'

for i in range(1, 12):
    url = tl % i
    print(url)
    content = req.get(url)
    ins = bs(content.text, 'html.parser')
    colleges = ins.find_all(name='a',attrs={"class":"institute-lite-logo"})
    import time
    for c in colleges:
        try:
            y = extract_info(c.get('href'))
            if y:
                print('page %d no %d' % (i, colleges.index(c)))
            time.sleep(0.3)
        except:
            pass

college_json = open('college2.json', 'w')
json.dump(college_set, college_json)


