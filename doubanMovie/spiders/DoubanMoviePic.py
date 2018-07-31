# -*- coding: utf-8 -*-
from scrapy.spiders import Spider
from scrapy import Request
import time
import urllib.parse
from doubanMovie.spiders.SaveData import SaveData


class DoubanMovieAward(Spider):
    name = 'doubanMoviePic'
    type = 'PIC'
    picUrl = 'https://movie.douban.com/subject/{}/photos?type=R&start={}&sortby=like&size=a&subtype=a'

    def start_requests(self):
        history = SaveData().query_media_history(self.type)[0][1]
        mediaAwardList = SaveData().query_media_data(history, 1)[0]
        if len(mediaAwardList) > 0:
            dataItem = mediaAwardList
            picUrl = self.get_pic_url(dataItem[1], 0)
            yield Request(picUrl, meta={'movieId': str(dataItem[1]), 'title': dataItem[2], 'picNum': 30}, callback=self.parse_movie_pic)

    def get_pic_url(self, movieId, picNum):
        return self.picUrl.format(movieId, picNum)

    def parse_movie_pic(self, response):
        if response.status == 200:
            picIds = response.selector.xpath("//ul[@class='poster-col3 clearfix']/li/attribute::data-id").extract()
            if len(picIds) != 0:
                print("图片id")
                dataList = []
                for picId in picIds:
                    data = {}
                    data['id'] = response.meta['movieId']
                    data['title'] = response.meta['title']
                    data['picId'] = picId
                    dataList.append(data)
                SaveData().save_media_pic_id(dataList)
                picUrl = self.get_pic_url(response.meta['movieId'], response.meta['picNum'])
                yield Request(picUrl, meta={'movieId': response.meta['movieId'], 'title': response.meta['title'], 'picNum': response.meta['picNum'] + 30}, callback=self.parse_movie_pic)
            else:
                history = SaveData().query_media_history(self.type)[0][1]
                mediaAwardList = SaveData().query_media_data(history + 1, 1)[0]
                SaveData().update_media_history(self.type)
                if len(mediaAwardList) > 0:
                    dataItem = mediaAwardList
                    picUrl = self.get_pic_url(dataItem[1], 0)
                    yield Request(picUrl, meta={'movieId': str(dataItem[1]), 'title': dataItem[2], 'picNum': 30}, callback=self.parse_movie_pic)
        elif response.status == 404:
            history = SaveData().query_media_history(self.type)[0][1]
            mediaAwardList = SaveData().query_media_data(history + 1, 1)[0]
            SaveData().update_media_history(self.type)
            if len(mediaAwardList) > 0:
                dataItem = mediaAwardList
                picUrl = self.get_pic_url(dataItem[1], 0)
                yield Request(picUrl, meta={'movieId': str(dataItem[1]), 'title': dataItem[2], 'picNum': 30},
                              callback=self.parse_movie_pic)
        elif response.status == 301 or response.status == 302:
            history = SaveData().query_media_history(self.type)[0][1]
            mediaAwardList = SaveData().query_media_data(history + 1, 1)[0]
            SaveData().update_media_history(self.type)
            time.sleep(10)
            if len(mediaAwardList) > 0:
                dataItem = mediaAwardList
                picUrl = self.get_pic_url(dataItem[1], 0)
                yield Request(picUrl, meta={'movieId': str(dataItem[1]), 'title': dataItem[2], 'picNum': 30},
                              callback=self.parse_movie_pic)

    # 下载影片
    def down_movie_pic(self, movieId, moviePicIds):
        item = DoubanMovieItem()
        item['movieId'] = movieId
        item['moviePicIds'] = moviePicIds
        yield item