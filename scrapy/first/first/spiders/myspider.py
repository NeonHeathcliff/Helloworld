# coding=UTF-8
import scrapy
from first.items import FirstItem
import sys
 
class MySpider(scrapy.Spider):
    name = "spiderbaidu"
    allowed_domains = ["baidu.com"]
    start_urls = [
        "https://tieba.baidu.com/f?kw=%E7%BD%91%E7%BB%9C%E7%88%AC%E8%99%AB&ie=utf-8",
        ]

    def parse(self, response):
       for line in response.xpath('//li[@class=" j_thread_list clearfix"]'):
            item=FirstItem()
            item['title'] = line.xpath('.//div[contains(@class,"threadlist_title pull_left j_th_tit ")]/a/text()').extract()
            item['author'] = line.xpath('.//div[contains(@class,"threadlist_author pull_right")]//span[contains(@class,"frs-author-name-wrap")]/a/text()').extract()
            item['reply'] = line.xpath('.//div[contains(@class,"col2_left j_threadlist_li_left")]/span/text()').extract()
            yield item