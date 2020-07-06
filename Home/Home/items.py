# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

import scrapy


class HomeItem(scrapy.Item):
    #一级页面：url、name
    url = scrapy.Field()
    name = scrapy.Field()
    #二级页面：价格、付款方式、租赁方式、
    # 类型、楼层、地区、地址
    price = scrapy.Field()
    pay_way = scrapy.Field()
    rent_way = scrapy.Field()

    home_type = scrapy.Field()
    floor = scrapy.Field()
    region = scrapy.Field()
    address = scrapy.Field()
