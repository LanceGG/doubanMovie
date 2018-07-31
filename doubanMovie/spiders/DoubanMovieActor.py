# -*- coding: utf-8 -*-
from scrapy.spiders import Spider
from scrapy import Request
import urllib.parse
from doubanMovie.spiders.SaveData import SaveData


class DoubanMovieAward(Spider):
    name = 'doubanMovieActor'
    type = 'ACTOR'

    def start_requests(self):
        history = SaveData().query_media_history(self.type)[0][1]
        mediaAwardList = SaveData().query_media_data(history, 1)[0]
        if len(mediaAwardList) > 0:
            dataItem = mediaAwardList
            acturl = 'https://movie.douban.com/celebrity/' + str(dataItem[1]) + '/'
            yield Request(acturl,
                          callback=self.parse_actor_detail)

    def parse_actor_detail(self, response):
        if response.status == 200:
            actor = {}
            # 取id
            actor['id'] = response.url.replace('https://movie.douban.com/celebrity/', '').replace('/', '')
            actorDetailTags = response.selector.xpath("//div[@class='info']/ul/li")
            for actorDetailTag in actorDetailTags:
                actorTag = ''.join(actorDetailTag.xpath("./span/text()").extract())
                if actorTag == 'imdb编号':
                    actorVal = ''.join(actorDetailTag.xpath("./a/text()").extract())
                else:
                    actorVal = actorDetailTag.xpath("./span/following::text()")[0].extract().replace(' ', '').replace(
                        '\n', '')
                actor[actorTag] = actorVal
            print ("演员Detail")
            print (actor)

        else:
            url = response.url
            print ("演员Detail" + response.status + ": 访问失败, 重新访问")
            yield Request(url, headers=self.headers, callback=self.parse_actor_detail)

