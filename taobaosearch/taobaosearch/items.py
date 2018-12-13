# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# https://doc.scrapy.org/en/latest/topics/items.html

from scrapy import Field,Item


class TaobaosearchItem(Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    datavalue=44
    id=Field()
    title=Field()
    pic_url=Field()
    detail_url=Field()
    view_price=Field()
    item_loc=Field()
    view_sales=Field()
    comment_count=Field()
    nick=Field()
