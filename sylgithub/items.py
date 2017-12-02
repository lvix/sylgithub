# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# http://doc.scrapy.org/en/latest/topics/items.html

import scrapy


class SylgithubItem(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    pass

class GitItem(scrapy.Item):
	name = scrapy.Field()
	update_time = scrapy.Field()
