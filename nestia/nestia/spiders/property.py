# -*- coding: utf-8 -*-
import scrapy
import json
import datetime
from nestia.items import PropertyItem


class PropertySpider(scrapy.Spider):
    name = 'PropertySpider'
    allowed_domains = ['nestia.com']
    start_urls = [
        'https://property.nestia.com/webapi/sale/v4.6/sales?price_min=100000&floor_area_min=250&order_by=1&offset=0&limit=100',
    ]

    def __init__(self):
        self.limit = 100
        self.offset = 0

    def parse(self, response):
        property_list = json.loads(response.body)

        for item in property_list:        
            propertyItem = PropertyItem()

            propertyItem['property_id'] = item['detail_id']
            propertyItem['price'] = item['price']
            propertyItem['number_of_beds'] = item['bedroom_type']
            propertyItem['number_of_baths'] = item['bathroom_type']
            propertyItem['area'] = item['floor_area']
            propertyItem['price_unit'] = item['psf']
            propertyItem['project_type'] =  item['property_type']
            propertyItem['district_id'] =  item['district_id']
            propertyItem['top'] =  item['top']
            propertyItem['latitude'] =  item['latitude']
            propertyItem['longitude'] =  item['longitude']

            propertyItem['project_id'] = item.get('project_id', -1)
            propertyItem['project_name'] = item.get('project_name', "")
            propertyItem['tenure'] =  item.get('tenure', -1)

            propertyItem['scraped_date'] = datetime.datetime.now

            yield propertyItem
        
        if len(property_list) == self.limit:
            self.offset += 100
            next_property_list_url = 'https://property.nestia.com/webapi/sale/v4.6/sales?price_min=100000&floor_area_min=250&order_by=1&offset=' + str(self.offset) + '&limit=' +  str(self.limit) 
            return scrapy.Request(next_property_list_url, callback=self.parse)