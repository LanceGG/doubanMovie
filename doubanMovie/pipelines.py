# -*- coding: utf-8 -*-
import requests
import sys
from doubanMovie.items import DoubanMovieItem
import scrapy
from scrapy.pipelines.images import ImagesPipeline
from scrapy.exceptions import DropItem
# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://doc.scrapy.org/en/latest/topics/item-pipeline.html


class DoubanmoviePipeline(object):

    def get_media_requests(self, item, info):
        for moviePicId in item['moviePicIds']:
            headers = {
                'Accept': 'application/json, text/plain, */*',
                'Accept-Encoding': 'gzip, deflate, br',
                'Accept-Language': 'zh-CN,zh;q=0.9',
                'Connection': 'keep-alive',
                'host': 'movie.douban.com',
                'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/67.0.3396.99 Safari/537.36',
                'Cookie': 'bid=Objb_yrj_J8; gr_user_id=4264a3ce-820b-4616-90e0-9a187466b3f1; ll="118172"; _vwo_uuid_v2=C9521AE5387ADFBF455CDF22AC9B6144|ab2fc29361bd1ebbeecca1fa6686d28c; viewed="5980062_26692216_3259440"; __utmz=30149280.1529829901.15.14.utmcsr=baidu|utmccn=(organic)|utmcmd=organic; __yadk_uid=02pWxtVnBlRpQHZwvaJOMHdftdnYeLRu; _pk_ses.100001.4cf6=*; __utma=30149280.1220139084.1501422800.1532363369.1532446977.18; __utmb=30149280.0.10.1532446977; __utmc=30149280; __utmc=223695111; __utma=223695111.1517590416.1532359178.1532446977.1532447181.4; __utmz=223695111.1532447181.4.2.utmcsr=baidu|utmccn=(organic)|utmcmd=organic; __utmt=1; dbcl2="62576053:2d22ZNUsOEk"; ck=T-u6; __utmb=223695111.19.10.1532447181; push_noty_num=0; push_doumail_num=0; _pk_id.100001.4cf6=001d12c5ce3d950f.1532359178.3.1532447860.1532364881.'}
            headers['Referer'] = 'https://movie.douban.com/photos/photo/{}/'.format(moviePicId)
            downPicUrl = 'https://img3.doubanio.com/view/photo/raw/public/p{}.jpg'.format(moviePicId)
            yield scrapy.Request(downPicUrl, headers=headers, meta={'movieId': item['movieId']})

    def item_completed(self, results, item, info):
        image_paths = [x['path'] for ok, x in results if ok]
        if not image_paths:
            raise DropItem("Item contains no images")
        item['image_paths'] = image_paths
        return item
