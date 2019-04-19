# -*- coding: utf-8 -*-
import scrapy
import json
from datetime import datetime
from nestia.items import SalePropertyItem
from scrapy.conf import settings


class SalePropertySpider(scrapy.Spider):
    name = 'sale_property'
    allowed_domains = ['nestia.com']

    def __init__(self, offset=0, *args, **kwargs):
        super(SalePropertySpider, self).__init__(*args, **kwargs)
        self.offset = offset
        self.limit = settings['SALE_PROPERTIES_LIMIT']
        self.start_urls = ['https://property.nestia.com/webapi/sale/v4.6/sales?price_min=100000&floor_area_min=250&order_by=8&offset=' +
                           str(self.offset) + '&limit=' + str(self.limit), ]

    def parse(self, response):
        items = []

        if response.status == 200:
            items = json.loads(response.body)

            for item in items:
                propertyItem = SalePropertyItem()

                propertyItem['id'] = item['detail_id']
                propertyItem['price'] = item['price']
                propertyItem['number_of_beds'] = item['bedroom_type']
                propertyItem['number_of_baths'] = item['bathroom_type']
                propertyItem['area'] = item['floor_area']
                propertyItem['price_unit'] = item['psf']
                propertyItem['project_type'] = item['property_type']
                propertyItem['district_id'] = item['district_id']
                propertyItem['sub_district_id'] = item['sub_district_id']
                propertyItem['top'] = item['top']
                propertyItem['latitude'] = item['latitude']
                propertyItem['longitude'] = item['longitude']
                propertyItem['project_id'] = item.get('project_id', -1)
                propertyItem['project_name'] = item.get('project_name', '')
                propertyItem['tenure'] = item.get('tenure', -1)
                propertyItem['address'] = item['display_name']
                propertyItem['postal_code'] = item.get('postal_code', -1)
                propertyItem['mrts'] = item.get('mrts', '')
                propertyItem['agent'] = item.get('user_profile', '')
                propertyItem['url'] = "https://property.nestia.com/for-sale/" + \
                    item['url_address'] + "/" + str(item['detail_id'])
                propertyItem['scraped_date'] = datetime.now().strftime(
                    '%Y-%m-%d %H:%M:%S')
                propertyItem['last_updated_date'] = datetime.now().strftime(
                    '%Y-%m-%d %H:%M:%S')

                yield propertyItem

        if (response.status == 200 and len(items) == self.limit) or response.status != 200:
            self.offset += self.limit
            next_property_list_url = 'https://property.nestia.com/webapi/sale/v4.6/sales?price_min=100000&floor_area_min=250&order_by=8&offset=' + \
                str(self.offset) + '&limit=' + str(self.limit)
            yield scrapy.Request(next_property_list_url, callback=self.parse)
