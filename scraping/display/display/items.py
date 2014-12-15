# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# http://doc.scrapy.org/en/latest/topics/items.html

import scrapy


class DisplayItem(scrapy.Item):
    title   = scrapy.Field()
    address = scrapy.Field()
    time    = scrapy.Field()
    url     = scrapy.Field()
    #seller  = scrapy.Field()
    #phone   = scrapy.Field()
    #price   = scrapy.Field()

