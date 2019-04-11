# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# https://doc.scrapy.org/en/latest/topics/items.html

from scrapy import Item, Field


class PropertyItem(Item):
    listing_id = Field()
    number_of_beds = Field()
    number_of_baths = Field()
    area = Field()
    price = Field()
    price_unit = Field()
    address = Field()
    postal_code = Field()
    property_type = Field()
    tenure = Field()
    psf = Field()
    developer = Field()
    floor_level = Field()
    listed_on = Field()
    maintenance_fee = Field()
    land_size = Field()
    furnishing = Field()
    top = Field()
    current_tenanted = Field()
    total_units = Field()
    key_features = Field()
    Facilities = Field()

class Agent(Item):
    agent_name = Field()
    agent_licence = Field()
    agency_name = Field()
    services = Field()
    regions_covered = Field()
    hdb_estates_covered = Field()
