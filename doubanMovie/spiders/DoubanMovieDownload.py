# -*- coding: utf-8 -*-
from scrapy.spiders import Spider
from scrapy import Request
import urllib.parse
from doubanMovie.items import DoubanMovieItem
from doubanMovie.spiders.SaveData import SaveData
import scrapy


class DoubanMovieDownLoad(Spider):

    name = 'doubanMovieDownload'
    type = 'PICDOWN'

    def start_requests(self):
        yield Request('https://movie.douban.com/subject/1295644/')

    def parse(self, response):
        item = DoubanMovieItem()
        history = SaveData().query_media_history(self.type)[0][1]
        mediaDataList = SaveData().query_media_data(history, 1)[0]
        # while len(mediaDataList) > 0:
        dataList = SaveData().query_media_pic_id(str(mediaDataList[1]))
        item['movieId'] = str(mediaDataList[1])
        item['moviePicIds'] = dataList
        yield item
        # SaveData().update_media_history(self.type)
        # history = history+1
        # mediaDataList = SaveData().query_media_data(history, 1)[0]