# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# https://doc.scrapy.org/en/latest/topics/items.html

from scrapy import Item, Field


class PropertyItem(Item):
    property_id = Field()
    price = Field()
    number_of_beds = Field()
    number_of_baths = Field()
    area = Field()
    price_unit = Field()
    project_type = Field()
    project = Field()
    district = Field()
    top = Field()
    tenure = Field()
    furnishing = Field()
    address = Field()
    posted_on = Field()
    description = Field()
    indoor_features = Field()
    outdoor_features = Field()
    special_features = Field()
