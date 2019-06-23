# -*- coding: utf-8 -*-
import pymongo
from douban.settings import mongo_host, mongo_port, mongo_db, mongo_collection

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://doc.scrapy.org/en/latest/topics/item-pipeline.html


class DoubanPipeline(object):

    def __init__(self):
        host = mongo_host
        port = mongo_port
        db = mongo_db
        collection = mongo_collection
        client = pymongo.MongoClient(host=host,port=port)
        mydb = client[db]
        self.post= mydb[collection]
    def process_item(self, item, spider):
        data = dict(item)
        self.post.insert(data)
        return item
