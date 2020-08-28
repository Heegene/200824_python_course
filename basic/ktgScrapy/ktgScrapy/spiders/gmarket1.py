# -*- coding: utf-8 -*-
import scrapy
import urllib

class Gmarket1Spider(scrapy.Spider):
    name = 'gmarket1'
    allowed_domains = ['www.gmarket.co.kr']
    start_urls = ['http://www.gmarket.co.kr/']

    def parse(self, response):
        print(response)
