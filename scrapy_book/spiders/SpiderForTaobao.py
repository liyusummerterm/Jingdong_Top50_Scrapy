import json
import re
from pprint import pprint
from urllib import parse
from scrapy_book.settings import *

import scrapy


class MytaobaoSpider(scrapy.Spider):
    name = 'mytaobao'
    allowed_domains = ['https://www.taobao.com']
    # 将搜索后的链接替换到列表中
    start_urls = ['https://s.taobao.com/search?q=%E8%A3%99%E5%AD%90&sort=sale-desc&s=44']

    def start_requests(self):
        for a in range (10):
            url='https://uland.taobao.com/sem/tbsearch?refpid=mm_26632258_3504122_32538762&keyword=%E4%B9%A6&clk1=940649a120c1376e753d50097334692c&upsId=940649a120c1376e753d50097334692c&spm=a2e0b.20350158.31919782.1&pid=mm_26632258_3504122_32538762&union_lens=recoveryid%3A201_11.132.162.80_2580771_1625623322106%3Bprepvid%3A201_11.132.162.80_2580771_1625623322106&pnum={}'.format(a)
            yield url

    def parse(self, response):
        pass
