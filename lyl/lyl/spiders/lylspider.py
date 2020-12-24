import scrapy
import random
import string
import json
import re
from ..items import LylItem

class LylSpider(scrapy.Spider):
    name = 'sou'

    def __init__(self, fpath=None):
        self.lujing = fpath

    def start_requests(self):
        t = open(self.lujing, 'r', encoding='UTF-8')
        list = re.findall('[1-9][0-9]?. .{4,20}', t.read())
        url = 'https://api.shuashuati.com/search/kuakeSearch'
        headers = {
            "Host": "api.shuashuati.com",
            "accept": "application/json, text/plain, */*",
            "origin": "https://spread.sm.cn",
            "user-agent": "Mozilla/5.0 (Linux; U; Android 10; zh-CN; Redmi K30 Build/PKQ1.190302.001) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/78.0.3904.108 Quark/4.5.3.153 Mobile Safari/537.36",
            "content-type": "application/json;charset\u003dUTF-8",
            "sec-fetch-site": "cross-site",
            "sec-fetch-mode": "cors",
            "referer": "https://spread.sm.cn/education/university/home?uc_param_str\u003ddsdnutlbgpmiosntnnfrpfbivepcsvpr\u0026entry\u003dnavi_add\u0026uc_biz_str\u003dOPT%3ABACK_BTN_STYLE%400%7Cqk_enable_gesture%3Afalse%7COPT%3ATOOLBAR_STYLE%400%7cOPT%3aS_BAR_BG_COLOR%40FFFFFF%7cOPT%3aW_PAGE_REFRESH%400",
            "accept-encoding": "gzip, deflate, br",
            "accept-language": "zh-CN,zh;q\u003d0.9,en-US;q\u003d0.8,en;q\u003d0.7"
        }
        for k in list:
            sid = str(''.join(random.sample(string.ascii_lowercase + string.digits, 32)))
            sip = '.'.join(map(str, random.sample(range(12, 126), 4))) + '.'
            keyword = k[3:]
            data = {"keyword": keyword, "userip": sip, "useriden": sid}
            yield scrapy.Request(url, method="POST", headers=headers, body=json.dumps(data), meta={'xuhao': k[0:3]}, dont_filter=True)

    def parse(self, response):
        item = LylItem()
        xuhao = response.meta['xuhao']
        req = response.json()
        item['xuhao'] = xuhao
        item['timu'] = req['data']['resultList'][0]['question'].replace('<br>', '\n')
        item['daan'] = req['data']['resultList'][0]['answer'].replace('<br>', '\n')
        yield item
