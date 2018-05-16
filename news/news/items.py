# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# https://doc.scrapy.org/en/latest/topics/items.html

import scrapy


class NewsItem(scrapy.Item):
    # define the fields for your item here like:
	Ticker = scrapy.Field()
	Url = scrapy.Field()
	Title = scrapy.Field()
	Summary = scrapy.Field()
	SourceName = scrapy.Field()
	SourceUrl = scrapy.Field()
	DateTime = scrapy.Field()