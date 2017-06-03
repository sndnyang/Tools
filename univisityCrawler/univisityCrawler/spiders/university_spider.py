# -*-coding: utf-8 -*-

import os
import json

import scrapy


class QuotesSpider(scrapy.Spider):
    name = "universities"

    allowed_domains = []

    def read_url_from_json(self):
        fname = os.path.join(os.path.dirname(__file__), 'college.json')
        college_json = open(fname)
        college_set = json.load(college_json)
        college_url = []
        for c in college_set:
            url = c['webpage']
            if url.find('//') > -1:
                college_url.append(url)
                url = url[url.find('//')+2:]
            else:
                college_url.append('http://' + url)

            # self.allowed_domains.append(url)
        return college_url

    def start_requests(self):
        urls = self.read_url_from_json()
        for url in urls:
            print(url)
            yield scrapy.Request(url=url, callback=self.parse)

    def parse(self, response):
        key_words = ['deadline', 'requirement', 'tuition', 'cost', 'international']
        for href in response.css("a::attr('href')"):
            
            print(href.extract())
            # yield response.follow(href, callback=self.parse)


