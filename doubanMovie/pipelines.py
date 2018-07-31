# -*- coding: utf-8 -*-
import requests
import sys
from doubanMovie.items import DoubanMovieItem
from scrapy.pipelines.images import ImagesPipeline
import scrapy
from scrapy.http import Request
# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://doc.scrapy.org/en/latest/topics/item-pipeline.html


class DoubanmoviePipeline(object):
    def process_item(self, item, spider):
        return item

class MyImagesPipeline(ImagesPipeline):
    def get_media_requests(self, item, info):
        for moviePicId in item['moviePicIds']:
            headers = {
                'Accept':'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8',
                'Accept-Encoding': 'gzip, deflate, br',
                'Accept-Language': 'zh-CN,zh;q=0.8,zh-TW;q=0.7,zh-HK;q=0.5,en-US;q=0.3,en;q=0.2',
                'cache-control': 'no-cache',
                'Connection': 'keep-alive',
                'Host': 'img3.doubanio.com',
                'Pragma': 'no-cache',
                'Upgrade-Insecure-Requests': '1',
                'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:61.0) Gecko/20100101 Firefox/61.0'
            }
            headers['Referer'] = 'https://movie.douban.com/subject/{}/'.format(item['movieId'])
            downPicUrl = 'https://img3.doubanio.com/view/photo/raw/public/p{}.jpg'.format(moviePicId[3])

            yield Request(downPicUrl, headers=headers, meta={'movieId': item['movieId'], 'moviePicId': moviePicId[3]})

    def file_path(self, request, response=None, info=None):
        movieId = request.meta['movieId']

        image_name = request.meta['moviePicId']
        return 'full/' + movieId + '/%s.jpg' % (image_name)
