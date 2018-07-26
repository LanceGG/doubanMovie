# -*- coding: utf-8 -*-
from scrapy.spiders import Spider
from scrapy import Request
import urllib.parse
from doubanMovie.spiders.SaveData import SaveData


class DoubanMoviePerform(Spider):
    name = 'doubanMoviePerform'

    def start_requests(self):
        history = SaveData().query_media_history('ACTOR')[0][1]
        mediaDataList = SaveData().query_media_data(history, 1)[0]
        if len(mediaDataList) > 0:
            dataItem = mediaDataList
            url = 'https://movie.douban.com/celebrity/' + str(actorId) + '/'
            yield Request(url, meta={'classify': dataItem['classify'], 'id': dataItem['id']},
                          callback=self.parse_actor_detail)

    def parse_actor_detail(self, response):
        actor = {}
        # 取id
        actor['id'] = response.url.replace('https://movie.douban.com/celebrity/', '').replace('/', '')
        actorDetailTags = response.selector.xpath("//div[@class='info']/ul/li")
        for actorDetailTag in actorDetailTags:
            actorTag = ''.join(actorDetailTag.xpath("./span/text()").extract())
            if actorTag == 'imdb编号':
                actorVal = ''.join(actorDetailTag.xpath("./a/text()").extract())
            else:
                actorVal = actorDetailTag.xpath("./span/following::text()")[0].extract().replace(' ', '').replace('\n',
                                                                                                                  '')
            actor[actorTag] = actorVal
            print ("演员Detail")
            print (actor)
