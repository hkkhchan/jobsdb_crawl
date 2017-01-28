# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# http://doc.scrapy.org/en/latest/topics/items.html

import scrapy


class JobsItem(scrapy.Item):
  position = scrapy.Field()
  company = scrapy.Field()
  address = scrapy.Field()
  link = scrapy.Field()
