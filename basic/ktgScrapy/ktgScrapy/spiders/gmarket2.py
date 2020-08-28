# -*- coding: utf-8 -*-
import scrapy


class Gmarket2Spider(scrapy.Spider):
    name = 'gmarket2'
    allowed_domains = ['http://corners.gmarket.co.kr/Bestsellers']
    start_urls = ['http://corners.gmarket.co.kr/Bestsellers/']

    def parse(self, response):
        titles = response.css('div.best-list li > a::text').getall()

        for title in titles:
            print("Title ->" , title)
