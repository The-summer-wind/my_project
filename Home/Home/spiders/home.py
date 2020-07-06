# -*- coding: utf-8 -*-
import scrapy
from ..items import HomeItem
import re


class HomeSpider(scrapy.Spider):
    name = 'home'
    allowed_domains = ['cq.58.com']
    start_urls = ['https://cq.58.com/chuzu/pn1']


    #生成URL地址变量
    n = 1
    def parse(self, response):
        li_list = response.xpath('//div[@class="des"]/h2')
        #给item.py中HomeItem类实例化
        item = HomeItem()
        for li in li_list:
            item['name'] = li.xpath('.//a').get().split('\n')[1]
            item['url'] = li.xpath('.//a[1]/@href').get()


            #把抓取的数据，传给管道文件
            yield item

        #当页数据抓取完成，生成下一页的URL地址，交给调度器入队列
        if self.n < 5:
            self.n += 1
            url = 'https://cq.58.com/chuzu/pn{}/'.format(self.n)
            #把url交给调度器入队列
            yield scrapy.Request(url=url,callback=self.parse)
