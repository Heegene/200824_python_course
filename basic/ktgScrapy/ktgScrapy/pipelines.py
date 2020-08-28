# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html
from scrapy.exceptions import DropItem

# 각 아이템 생성시, pipeline.py 에 있는 process_item 함수를 거쳐가게 되어 있음
# gmarket5 에서 적용
class KtgscrapyPipeline(object):
    def process_item(self, item, spider):
        print(item)
        if item['price'] > 10000:
            return item
        else:
            raise DropItem("drop item having lower price than 10000")
