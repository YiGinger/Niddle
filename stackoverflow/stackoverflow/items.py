# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# http://doc.scrapy.org/en/latest/topics/items.html

from scrapy.item import Item, Field


class StackoverflowItem(Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    company=Field()
    jobtitle=Field()
    job_url=Field()
    job_tag=Field()
    location=Field()
    time=Field()
    pass
