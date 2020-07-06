# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html



class HomePipeline:
    def process_item(self, item, spider):
        print(dict(item))
        return item

import pymysql
from .settings import *

class HomeMysqlPipeline(object):
    def open_spider(self,spider):
    # """爬虫项目启动时只执行1次,一般用于数据库连接"""        
        self.db = pymysql.connect(MYSQL_HOST,MYSQL_USER,MYSQL_PWD,MYSQL_DB,charset=CHARSET)
        self.cursor = self.db.cursor()
    def process_item(self,item,spider):
        """处理从爬虫文件传过来的item数据"""
        ins = 'insert into hometab values(%s,%s)'
        Home_li = [item['url'],item['name']]
        self.cursor.execute(ins,Home_li)
        self.db.commit()
        return item
    def close_spider(self,spider):
        """爬虫程序结束时只执行1次,一般用于数据库断开"""
        self.cursor.close()
        self.db.close()


# import pymongo
#
#
# class HomeMongoPipeline(object):
#     def open_spider(self, spider):
#         self.conn = pymongo.MongoClient(localhost,27017)
#         self.db = self.conn[MONGO_DB]
#         self.myset = self.db[MONGO_SET]
#
#     def process_item(self, item, spider):  
#         Home_dict = {
#             'url':item['url'],
#             'name':item['name'],
#         }
#         self.myset.insert_one(Home_dict)
#


