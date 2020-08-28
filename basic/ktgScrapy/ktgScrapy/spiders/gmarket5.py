# -*- coding: utf-8 -*-
# KtgscrapyItem 의 title/price를 가져오되, PipeLine를 거쳐서
# 가져오게 만듦
import scrapy
from  ktgScrapy.items import KtgscrapyItem

class Gmarket5Spider(scrapy.Spider):
    name = 'gmarket5'
    allowed_domains = ['corners.gmarket.co.kr/Bestsellers']
    start_urls = ['http://corners.gmarket.co.kr/Bestsellers/']

    def parse(self, response):
        titles = response.css('div.best-list > ul > li[id] > a::text').getall()
        prices = response.css('div.best-list > ul > li[id] > div.item_price > div.s-price > strong > span > span::text').getall()
        for i in range(len(titles)):
            item = KtgscrapyItem()
            item['title'] = titles[i]
            item['price'] = int(prices[i].replace("원", "").replace(",", ""))
            yield item