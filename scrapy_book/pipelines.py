# -*- coding: utf-8 -*-
from random import *

from model.book import Book
# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://doc.scrapy.org/en/latest/topics/item-pipeline.html
import codecs
import json

from model.book_picture import BookPicture


class ScrapyBookPipeline(object):
    def __init__(self):
        self.file = codecs.open('data.json', 'w', encoding='utf-8')

    def process_item(self, item, spider):
        print(item)
        line = json.dumps(dict(item), ensure_ascii=False) + "\n"
        self.file.write(line)
        book = Book(isbn='', book_name=item['title'], owner_id=41, category_id=0, price=randint(25, 120),
                    author=item['author'], press=item['publisher'], description=item['des'], status=0)
        book.save()
        BookPicture.insert(book_id=book.id, pic_url=item['s_img']).execute()

        return item

    def spider_closed(self, spider):
        self.file.close()
