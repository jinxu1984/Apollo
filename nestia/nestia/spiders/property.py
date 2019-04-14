# -*- coding: utf-8 -*-
import scrapy
import json
from datetime import datetime
from nestia.items import PropertyItem


class PropertySpider(scrapy.Spider):
    name = 'PropertySpider'
    allowed_domains = ['nestia.com']
    start_urls = [
        'https://property.nestia.com/webapi/sale/v4.6/sales?price_min=100000&floor_area_min=250&order_by=1&offset=0&limit=10',
    ]

    def __init__(self):
        self.limit = 10
        self.offset = 0

    def parse(self, response):
        if response.status != 200:
            print(response.status)
        else:
            items = json.loads(response.body)
                
            for item in items:
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
                propertyItem['address'] =  item['display_name']
                propertyItem['postal_code'] =  item.get('postal_code', -1)
                propertyItem['scraped_date'] = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
                propertyItem['agent'] = item.get('user_profile', "")

                yield propertyItem
            
            if len(items) == self.limit:
                self.offset += self.limit
                next_property_list_url = 'https://property.nestia.com/webapi/sale/v4.6/sales?price_min=100000&floor_area_min=250&order_by=1&offset=' + str(self.offset) + '&limit=' +  str(self.limit) 
                yield scrapy.Request(next_property_list_url, callback=self.parse)