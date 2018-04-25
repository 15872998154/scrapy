# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# https://doc.scrapy.org/en/latest/topics/items.html

import scrapy


class TencentnextItem(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    positionName = scrapy.Field()
    positionType = scrapy.Field()
    peopleCount  = scrapy.Field()
    workPlace    = scrapy.Field()
    publicTime   = scrapy.Field()


