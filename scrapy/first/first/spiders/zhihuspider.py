# coding=UTF-8
import scrapy
from first.items import FirstItem
import sys
 
class MySpider(scrapy.Spider):
    name = "spiderzhihu"
    allowed_domains = ["zhihu.com"]
    start_urls = [
        "https://www.zhihu.com/question/365438035",
        ]

    def parse(self, response):
       a=1
       for line in response.xpath('//li[@class="List-item"]'):
            item=FirstItem()
            item['answer'] = a
            item['title'] = line.xpath('.//div[contains(@class,"ContentItem AnswerItem")]//h2/text()').extract()
            item['word'] = line.xpath('.//div[contains(@class,"ContentItem AnswerItem")]//p/text()').extract()
            a+=1
            yield item