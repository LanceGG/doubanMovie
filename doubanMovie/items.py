# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# https://doc.scrapy.org/en/latest/topics/items.html

import scrapy


class DoubanMovieItem(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    headers = scrapy.Field() #
    detailURL = scrapy.Field()  # 图片原图地址
    title = scrapy.Field()  # 标题
    fileName = scrapy.Field()  # 文件夹名
    path = scrapy.Field()  # 图片存储路径（绝对路径）

