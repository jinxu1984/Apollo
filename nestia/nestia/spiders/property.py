# -*- coding: utf-8 -*-
import scrapy
import json
from nestia.items import PropertyItem


class PropertySpider(scrapy.Spider):
    name = 'PropertySpider'
    allowed_domains = ['nestia.com']
    start_urls = [
        'https://property.nestia.com/webapi/sale/v4.6/sales?price_min=100000&floor_area_min=250&order_by=1&offset=0&limit=10',
    ]

    def parse(self, response):
        #offset = 0
        property_list = json.loads(response.body)

        for propertyItem in property_list:
            property_details_url = 'https://property.nestia.com/for-sale/' + propertyItem["url_address"] + '/' + str(propertyItem["detail_id"])
            yield scrapy.Request(property_details_url, callback=self.parse_property)
        
    def parse_property(self, response):
        propertyItem = PropertyItem()

        #propertyItem['property_id'] = response.xpath("//div[@class='property-attr']").extract()
        propertyItem['price'] = response.xpath('//span[@class="money"]/text()').extract()[0]
        propertyItem['number_of_beds'] = response.xpath('//div[@class="typegroup"]/div[@class="type"][1]/span[@class="text"]/text()').extract()[0]
        propertyItem['number_of_baths'] = response.xpath('//div[@class="typegroup"]/div[@class="type"][2]/span[@class="text"]/text()').extract()[0]
        propertyItem['area'] = response.xpath('//div[@class="typegroup"]/div[@class="type"][3]/span[@class="text"]/text()').extract()[0]
        propertyItem['price_unit'] = response.xpath('//div[@class="typegroup"]/div[@class="type"][4]/span[@class="text"]/text()').extract()[0]
        propertyItem['project_type'] =  response.xpath('//div[@class="info"]/div[@class="item"][1]/span[@class="con"]/text()').extract()[0]
        propertyItem['project'] =  response.xpath('//div[@class="info"]/div[@class="item"][2]/span[@class="con"]/a/text()').extract()[0]
        propertyItem['district'] =  response.xpath('//div[@class="info"]/div[@class="item"][3]/span[@class="con"]/text()').extract()[0]
        propertyItem['top'] =  response.xpath('//div[@class="info"]/div[@class="item"][4]/span[@class="con"]/text()').extract()[0]
        propertyItem['tenure'] =  response.xpath('//div[@class="info"]/div[@class="item"][5]/span[@class="con"]/text()').extract()[0]
        propertyItem['address'] =  response.xpath('//div[@class="info"]/div[@class="item"][6]/span[@class="con"]/text()').extract()[0]
        propertyItem['posted_on'] =  response.xpath('//div[@class="info"]/div[@class="item item-update"][1]/span/text()').extract()[0]
        #propertyItem['description'] = response.xpath('//div[@class="m-description-bd js-title-hook"]/div[@class="item item-line"][1]/div[@class="con"]/text()').extract()
        propertyItem['indoor_features'] = response.xpath('//div[@class="m-amenities-item"][1]/div/ul/li/span/text()').extract()
        propertyItem['outdoor_features'] = response.xpath('//div[@class="m-amenities-item"][2]/div/ul/li/span/text()').extract()
        propertyItem['special_features'] = response.xpath('//div[@class="m-amenities-item"][3]/div/ul/li/span/text()').extract()

        return propertyItem