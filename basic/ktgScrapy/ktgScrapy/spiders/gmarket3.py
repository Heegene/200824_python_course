# -*- coding: utf-8 -*-
import scrapy
from  ktgScrapy.items import KtgscrapyItem

class Gmarket3Spider(scrapy.Spider):
    name = 'gmarket3'
    allowed_domains = ['http://corners.gmarket.co.kr/Bestsellers']
    start_urls = ['http://corners.gmarket.co.kr/Bestsellers/']

    def parse(self, response):
        titles = response.css('div.best-list li > a::text').getall()
        for title in titles:
            item = KtgscrapyItem()
            item['title'] = title
            yield item
