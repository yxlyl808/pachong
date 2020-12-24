# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

import scrapy

class LylItem(scrapy.Item):
    xuhao = scrapy.Field()  # 题目序号
    timu = scrapy.Field()  # 题目
    daan = scrapy.Field()  # 答案
