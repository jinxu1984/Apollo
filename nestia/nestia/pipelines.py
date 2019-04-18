# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://doc.scrapy.org/en/latest/topics/item-pipeline.html
import json
import csv
from datetime import datetime
from pymongo import MongoClient
from scrapy.conf import settings
from scrapy import signals
from scrapy.exporters import JsonLinesItemExporter
from scrapy.exporters import CsvItemExporter

class CsvWriterPipeline(object):
    
    def __init__(self):
        self.file = open('output.csv', 'w+b')
        self.exporter = CsvItemExporter(self.file)
        self.exporter.start_exporting()

    def close_spider(self, spider):
        self.exporter.finish_exporting()
        self.file.close()

    def process_item(self, item, spider):
        self.exporter.export_item(item)
        return item

class JsonWriterPipeline(object):

    def __init__(self):
        self.file = open('properties.json', 'wb')
        self.exporter = JsonLinesItemExporter(self.file, encoding='utf-8', ensure_ascii=False)
        self.exporter.start_exporting()

    def close_spider(self, spider):
        self.exporter.finish_exporting()
        self.file.close()

    def process_item(self, item, spider):
        self.exporter.export_item(item)
        return item

class CosmosPipeline(object):

    def __init__(self): 
        self.client = MongoClient(settings['COSMOSDB_URL'])

    def open_spider(self, spider):
        db = self.client[settings['COSMOSDB_DATABASE']]
        db.authenticate(name=settings['COSMOSDB_USERNAME'],password=settings['COSMOSDB_KEY'])
        self.collection = db[settings['COSMOSDB_COLLECTION']]

    def close_spider(self, spider):
        self.client.close()

    def process_item(self, item, spider):
        existingProperties = self.collection.find({},{ "property_id": item['property_id']})
        
        if len(existingProperties) == 1:
            self.collection.update_one({ "property_id": item['property_id']}, { "$set": { "last_updated_date": datetime.now().strftime('%Y-%m-%d %H:%M:%S') } })
        else:
            self.collection.insert_one(dict(item))
                   
        return item