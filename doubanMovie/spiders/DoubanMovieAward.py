# -*- coding: utf-8 -*-
from scrapy.spiders import Spider
from scrapy import Request
import urllib.parse
from doubanMovie.spiders.SaveData import SaveData


class DoubanMovieAward(Spider):
    name = 'doubanMovieAward'

    def start_requests(self):
        history = SaveData().query_media_history('AWARD')[0][1]
        mediaDataList = SaveData().query_media_data(history, 1)[0]
        if len(mediaDataList) > 0:
            dataItem = mediaDataList
            awardUrl = dataItem[4] + 'awards/'
            yield Request(awardUrl,
                          meta={'classify': dataItem[5], 'id': dataItem[1], 'title': dataItem[2]},
                          callback=self.parse_movie_reward)

    def parse_movie_reward(self, response):
        movieReward = {}
        movieReward['id'] = response.meta['id']
        movieReward['title'] = response.meta['title']
        awardTypeList = []
        awardTypeTagList = response.selector.xpath("//div[@class='awards']")
        for awardTypeTag in awardTypeTagList:
            awardType = {}
            awardType['name'] = ''.join(awardTypeTag.xpath("./div/h2/a/text()").extract())
            awardType['year'] = ''.join(awardTypeTag.xpath("./div/h2/span/text()").extract())[2:6]
            awardList = []
            awardTagList = awardTypeTag.xpath("./ul")
            for awardTag in awardTagList:
                award = {}
                award['name'] = ''.join(awardTag.xpath("./li")[0].xpath("./text()").extract())
                awardUserList = []
                awardUserTagList = awardTag.xpath("./li")[1].xpath("./a")
                for awardUserTag in awardUserTagList:
                    awardUser = {}
                    awardUser['id'] = ''.join(awardUserTag.xpath("./attribute::href").extract()).replace(
                        'https://movie.douban.com/celebrity/', '').replace('/', '')
                    awardUser['name'] = ''.join(awardUserTag.xpath("./text()").extract())
                    awardUserList.append(awardUser)
                award['awardUserList'] = awardUserList
                awardList.append(award)
            awardType['awardList'] = awardList
            awardTypeList.append(awardType)
        movieReward['awardTypeList'] = awardTypeList
        print ("影片Reward")
        print (movieReward)
