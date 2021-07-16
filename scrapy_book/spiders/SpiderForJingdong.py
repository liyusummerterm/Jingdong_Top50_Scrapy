# -*- coding: utf-8 -*-
import scrapy

from scrapy_book.items import ScrapyBookItem


class SpiderForJingdong(scrapy.Spider):
    name = 'spider_xpath_jingdong'

    def start_requests(self):
        for i in range(5):
            url = 'https://book.jd.com/booktop/0-0-0.html?category=1713-0-0-0-10001-{}#comfort'.format(i)
            yield scrapy.Request(url=url, callback=self.parse)

    def parse(self, response):
        items = []
        print(response)
        for book in response.xpath("//ul[@class='clearfix']//li"):
            item = ScrapyBookItem()
            title = book.xpath("./div[@class='p-detail']//a[@class='p-name']//@title").extract_first().replace('\n',
                                                                                                               '').strip()
            sub_url = book.xpath("./div[@class='p-detail']//a[@class='p-name']//@href").extract_first().replace('\n',
                                                                                                                '').strip()
            publisher = book.xpath("./div[@class='p-detail']//dl[2]//dd//a//@title").extract_first().replace('\n',
                                                                                                             '').strip()
            price = book.xpath("./div[@class='p-detail']//dl[3]//dd//del").extract_first().replace('\n',
                                                                                                   '').strip()
            picture = book.xpath("./div[@class='p-img']//a//img//@data-lazy-img").extract_first().replace('\n',
                                                                                                          '').strip()
            author = book.xpath("./div[@class='p-detail']//dl[1]//dd//a//@title").extract_first().replace('\n',
                                                                                                  '').strip()
            print(title)
            item["title"] = title
            item["publisher"] = publisher
            item["price"] = 0
            sub_url = 'http:' + sub_url
            item["sub_url"] = sub_url
            item["s_img"] = picture
            item["author"] = author
            item['des'] = title + ' ' + publisher + ' ' + author + ' ' + sub_url
            items.append(item)
            # yield scrapy.Request(url=sub_url, callback=self.parse_second, meta={"item": item})
            # title2 = "无" if book.xpath("./tr/td[2]/div[1]/span/text()").extract_first() == None else book.xpath(
            #     "./tr/td[2]/div[1]/span/text()").extract_first().replace('\n', '').strip()
            # item['title'] = title1 + "(" + title2 + ")"
            # item['s_img'] = book.xpath("./tr/td[1]/a/img/@src").extract_first().replace('\n', '').strip()
            # item['scrible'] = "无" if book.xpath("./tr/td[2]/p[2]/span/text()").extract_first() == None else book.xpath(
            #     "./tr/td[2]/p[2]/span/text()").extract_first().replace('\n', '').strip()
            # sub_url = book.xpath("./tr/td[2]/div/a/@href").extract_first().replace('\n', '').strip()
            # items.append(item)
            #
            # # meta={"item":item} 传递item引用SinaItem对象
        return items

    # def parse_second(self, response):
    #     item = response.meta["item"]
    #     for book in response.xpath('//div[@class="p-parameter"]/ul'):
    #         isbn = book.xpath("./li[2]//@title").extract_first().replace('\n', '').strip()
    #         des = book.xpath("./div[@class='detail-tag-id-3']/div[2]/div/p/@text()")
    #         item["isbn"] = isbn
    #         item['des'] = des
        # book = response.xpath('//div[@class="indent"]/div').extract_first()
        # item["author"] = book.xpath("./div[1]/a[1]/text()").extract_first().replace('\n', '').strip()
        # item["publisher"] = book.xpath("./div[1]/a/@href").extract_first().replace('\n', '').strip()
        # item["pub_date"] = book.xpath("./div[1]/a/@href").extract_first().replace('\n', '').strip()
        # item["price"] = book.xpath("./div[1]/a/@href").extract_first().replace('\n', '').strip()
        # item["m_img"] = book.xpath("./div[1]/a/@href").extract_first().replace('\n', '').strip()
        # item["b_img"] = book.xpath("./div[1]/a/@href").extract_first().replace('\n', '').strip()
        # item["isbn"] = book.xpath("./div[2]/a[1]/text()").extract_first().replace('\n', '').strip()
        # yield item
