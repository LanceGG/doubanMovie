# -*- coding: utf-8 -*-
from scrapy.spiders import Spider
from scrapy import Request
import time
import urllib.parse
from doubanMovie.spiders.SaveData import SaveData


class DoubanMovieAward(Spider):
    name = 'doubanMovieAward'
    type = 'AWARD'

    def start_requests(self):
        history = SaveData().query_media_history(self.type)[0][1]
        mediaAwardList = SaveData().query_media_data(history, 1)[0]
        if len(mediaAwardList) > 0:
            dataItem = mediaAwardList
            awardUrl = dataItem[4] + 'awards/'
            yield Request(awardUrl,
                          meta={'history': history + 1, 'id': str(dataItem[1]), 'title': dataItem[2]},
                          callback=self.parse_movie_reward)

    def parse_movie_reward(self, response):
        if response.status == 200:
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
            dataList = self.get_award_sql(movieReward)
            SaveData().save_media_award(dataList)
            SaveData().update_media_history(self.type)
            print ("影片Reward")

            mediaAwardList = SaveData().query_media_data(response.meta['history'], 1)[0]
            if len(mediaAwardList) > 0:
                dataItem = mediaAwardList
                awardUrl = dataItem[4] + 'awards/'
                yield Request(awardUrl,
                              meta={'id': str(dataItem[1]), 'title': dataItem[2],
                                    'history': response.meta['history'] + 1},
                              callback=self.parse_movie_reward)
        elif response.status == 404:
            SaveData().update_media_history(self.type)
            mediaAwardList = SaveData().query_media_data(response.meta['history'], 1)[0]
            if len(mediaAwardList) > 0:
                dataItem = mediaAwardList
                awardUrl = dataItem[4] + 'awards/'
                yield Request(awardUrl,
                              meta={'id': str(dataItem[1]), 'title': dataItem[2],
                                    'history': response.meta['history'] + 1},
                              callback=self.parse_movie_reward)
        elif response.status == 301 or response.status == 302:
            # SaveData().update_media_history(self.type)
            time.sleep(10)
            mediaAwardList = SaveData().query_media_data(response.meta['history'], 1)[0]
            if len(mediaAwardList) > 0:
                dataItem = mediaAwardList
                awardUrl = dataItem[4] + 'awards/'
                yield Request(awardUrl,
                              meta={'id': str(dataItem[1]), 'title': dataItem[2],
                                    'history': response.meta['history'] + 1},
                              callback=self.parse_movie_reward)


    def get_award_sql(self, movieReward):
        dataList = []
        if len(movieReward['awardTypeList']) > 0:
            for awardType in movieReward['awardTypeList']:
                if len(awardType['awardList']) > 0:
                    for award in awardType['awardList']:
                        if len(award['awardUserList']) > 0:
                            for user in award['awardUserList']:
                                data = {}
                                data['id'] = movieReward['id']
                                data['title'] = movieReward['title']
                                data['awardName'] = awardType['name']
                                data['awardYear'] = awardType['year']
                                data['awardType'] = award['name']
                                data['awardUserId'] = user['id']
                                data['awardUserName'] = user['name']
                                dataList.append(data)
                        else:
                            data = {}
                            data['id'] = movieReward['id']
                            data['title'] = movieReward['title']
                            data['awardName'] = awardType['name']
                            data['awardYear'] = awardType['year']
                            data['awardType'] = award['name']
                            data['awardUserId'] = ''
                            data['awardUserName'] = ''
                            dataList.append(data)
                else:
                    data = {}
                    data['id'] = movieReward['id']
                    data['title'] = movieReward['title']
                    data['awardName'] = awardType['name']
                    data['awardYear'] = awardType['year']
                    data['awardType'] = ''
                    data['awardUserId'] = ''
                    data['awardUserName'] = ''
                    dataList.append(data)
        else:
            data = {}
            data['id'] = movieReward['id']
            data['title'] = movieReward['title']
            data['awardName'] = ''
            data['awardYear'] = ''
            data['awardType'] = ''
            data['awardUserId'] = ''
            data['awardUserName'] = ''
            dataList.append(data)

        return dataList