# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html


# useful for handling different item types with a single interface
from itemadapter import ItemAdapter


class LylPipeline:
    def __init__(self):
        self.d = open('答案.txt', 'w', encoding='UTF-8')

    def process_item(self, item, spider):
        self.d.write(item['xuhao']+item['timu']+'\n')
        self.d.write('答案：'+item['daan']+'\n')
        return item

    def close_spider(self, spider):
        self.d.close()
