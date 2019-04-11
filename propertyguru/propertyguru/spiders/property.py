# -*- coding: utf-8 -*-
import scrapy
from propertyguru.items import PropertyItem


class PropertySpider(scrapy.Spider):
    name = 'PropertySpider'
    start_urls = [
        'https://www.propertyguru.com.sg/listing/21717831/for-sale-the-esta',
    ]

    def parse(self, response):
        propertyItem = PropertyItem()

        propertyItem['listing_id'] = response.xpath("//div[@class='property-attr']").extract()
        # propertyItem['number_of_beds'] = response.xpath("li/h2/text()").extract()
        # propertyItem['number_of_baths'] = response.xpath("li/h2/text()").extract()
        # propertyItem['area'] = response.xpath("li/h2/text()").extract()
        # propertyItem['price'] = response.xpath("li/h2/text()").extract()
        # propertyItem['price_unit'] = response.xpath("li/h2/text()").extract()
        # propertyItem['address'] = response.xpath("li/h2/text()").extract()
        # propertyItem['postal_code'] = response.xpath("li/h2/text()").extract()
        # propertyItem['property_type'] = response.xpath("li/h2/text()").extract()
        # propertyItem['tenure'] = response.xpath("li/h2/text()").extract()
        # propertyItem['psf'] = response.xpath("li/h2/text()").extract()
        # propertyItem['developer'] = response.xpath("li/h2/text()").extract()
        # propertyItem['floor_level'] = response.xpath("li/h2/text()").extract()
        # propertyItem['listed_on'] = response.xpath("li/h2/text()").extract()
        # propertyItem['maintenance_fee'] = response.xpath("li/h2/text()").extract()
        # propertyItem['land_size'] = response.xpath("li/h2/text()").extract()
        # propertyItem['furnishing'] = response.xpath("li/h2/text()").extract()
        # propertyItem['top'] = response.xpath("li/h2/text()").extract()
        # propertyItem['current_tenanted'] = response.xpath("li/h2/text()").extract()
        # propertyItem['total_units'] = response.xpath("li/h2/text()").extract()
        # propertyItem['key_features'] = response.xpath("li/h2/text()").extract()
        # propertyItem['Facilities'] = response.xpath("li/h2/text()").extract()

        return propertyItem