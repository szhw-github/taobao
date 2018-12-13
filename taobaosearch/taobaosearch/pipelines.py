# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://doc.scrapy.org/en/latest/topics/item-pipeline.html
from pymongo import MongoClient,ASCENDING
from taobaosearch.settings import MONGO_DB,MONGO_URI,MONGO_CO
from log import log



class TaobaosearchPipeline(object):
    def __init__(self):
        self.__client=MongoClient(MONGO_URI)
        self.__db=self.__client[MONGO_DB]
        self.__collection=self.__db[MONGO_CO]
        self.__collection.create_index([('nid', ASCENDING)], unique=True)


    def process_item(self,item,spider):
        log('process item')
        try:
            self.__collection.insert_one(dict(item))
            log('succeed:insert db')
        except:
            log('warning:nid has been in the db ')
        return item

    def close_spider(self,spider):
        self.__client.close()



