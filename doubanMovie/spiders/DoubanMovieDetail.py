# -*- coding: utf-8 -*-
from scrapy.spiders import Spider
from scrapy import Request
import time
import urllib.parse
from doubanMovie.spiders.SaveData import SaveData


class DoubanMovieDetail(Spider):
    name = 'doubanMovieDetail'
    type = 'DETAIL'

    def start_requests(self):
        history = SaveData().query_media_history(self.type)[0][1]
        mediaDataList = SaveData().query_media_data(history, 1)[0]
        if len(mediaDataList) > 0:
            dataItem = mediaDataList
            yield Request(dataItem[4],
                          meta={'classify': dataItem[5], 'id': str(dataItem[1]), 'title': dataItem[2],
                                'history': history + 1},
                          callback=self.parse_movie_detail)

    def parse_movie_detail(self, response):
        if response.status == 200:
            movieDetail = {}
            # ID(ALL)
            id = response.meta['id']
            movieDetail['id'] = id

            # 标题(ALL)
            movieDetail['title'] = response.meta['title']

            # 剧集标题(ALL)
            titleLong = ''.join(response.selector.xpath('//span[@property="v:itemreviewed"]/text()').extract())
            movieDetail['titleLong'] = titleLong

            # 年份(ALL)
            year = ''.join(response.selector.xpath("//span[@class='year']/text()").extract())[1:5]
            movieDetail['year'] = year

            # 分类(ALL)
            classify = response.meta['classify']
            movieDetail['classify'] = classify

            # 导演(ALL)
            directorTagList = response.selector.xpath("//span[contains(text(),'导演')]/../span[@class='attrs']/a")
            directorList = []
            for directorTag in directorTagList:
                director = {}
                director['id'] = ''.join(directorTag.xpath('./attribute::href').extract()).replace('/celebrity/',
                                                                                                   '').replace('/', '')
                director['name'] = ''.join(directorTag.xpath('./text()').extract())
                directorList.append(director)
            movieDetail['directorList'] = directorList

            # 编剧(ALL)
            writerTagList = response.selector.xpath("//span[contains(text(),'编剧')]/../span[@class='attrs']/a")
            writerList = []
            for writerTag in writerTagList:
                writer = {}
                writer['id'] = ''.join(writerTag.xpath('./attribute::href').extract()).replace('/celebrity/', '').replace(
                    '/', '')
                writer['name'] = ''.join(writerTag.xpath('./text()').extract())
                writerList.append(writer)
            movieDetail['writerList'] = writerList

            # 主演(ALL)
            performerTagList = response.selector.xpath("//span[contains(text(),'主演')]/../span[@class='attrs']/a")
            performerList = []
            for performerTag in performerTagList:
                performer = {}
                performer['id'] = ''.join(performerTag.xpath('./attribute::href').extract()).replace('/celebrity/',
                                                                                                     '').replace('/', '')
                performer['name'] = ''.join(performerTag.xpath('./text()').extract())
                performerList.append(performer)
            movieDetail['performerList'] = performerList

            # 类型(ALL)
            type = ','.join(response.selector.xpath("//span[@property='v:genre']/text()").extract())
            movieDetail['type'] = type

            # 制片国家/地区(ALL)
            country = ''.join(response.selector.xpath("//span[contains(text(), '制片国家/地区')]/following::text()[1]").extract())
            movieDetail['country'] = country

            # 语言(ALL)
            language = ''.join(response.selector.xpath("//span[contains(text(), '语言')]/following::text()[1]").extract())
            movieDetail['language'] = language

            # 上映日期(ALL)
            releaseDate = ','.join(response.selector.xpath("//span[@property='v:initialReleaseDate']/text()").extract())
            movieDetail['releaseDate'] = releaseDate

            # 片长(ALONG)
            runtime = ''.join(response.selector.xpath("//span[@property='v:runtime']/text()").extract())
            movieDetail['runtime'] = runtime

            # 季数(MULTI)
            season = ''.join(
                response.selector.xpath("//select[@id='season']/option[@selected='selected']/text()").extract())
            movieDetail['season'] = season

            # 集数(MULTI)
            episodes = ''.join(
                response.selector.xpath("//span[contains(text(), '集数')]/following::text()[1]").extract()).replace(' ',
                                                                                                                  '').replace(
                '\n', '')
            movieDetail['episodes'] = episodes

            # 单集片长(MULTI)
            alongRuntime = ''.join(
                response.selector.xpath("//span[contains(text(), '单集片长')]/following::text()[1]").extract())
            movieDetail['alongRuntime'] = alongRuntime

            # 又名(ALL)
            alias = ''.join(response.selector.xpath("//span[contains(text(), '又名')]/following::text()[1]").extract())
            movieDetail['alias'] = alias

            # IMDbId(ALL)
            imdbId = ''.join(response.selector.xpath("//span[contains(text(), 'IMDb链接')]/following::a[1]/text()").extract())
            movieDetail['imdbId'] = imdbId

            # 评分(ALL)
            score = ''.join(response.selector.xpath("//strong[@class='ll rating_num']/text()").extract())
            movieDetail['score'] = score

            # 评分等级(ALL)
            rating = {}
            rating['stars5'] = ''.join(
                response.selector.xpath("//span[@class='stars5 starstop']/../span[@class='rating_per']/text()").extract())
            rating['stars4'] = ''.join(
                response.selector.xpath("//span[@class='stars4 starstop']/../span[@class='rating_per']/text()").extract())
            rating['stars3'] = ''.join(
                response.selector.xpath("//span[@class='stars3 starstop']/../span[@class='rating_per']/text()").extract())
            rating['stars2'] = ''.join(
                response.selector.xpath("//span[@class='stars2 starstop']/../span[@class='rating_per']/text()").extract())
            rating['stars1'] = ''.join(
                response.selector.xpath("//span[@class='stars1 starstop']/../span[@class='rating_per']/text()").extract())
            rating['peopleNum'] = ''.join(response.selector.xpath("//span[@property='v:votes']/text()").extract())
            movieDetail['rating'] = rating

            # 标签(ALL)
            tags = ','.join(response.selector.xpath("//div[@class='tags-body']/a/text()").extract())
            movieDetail['tags'] = tags

            # 剧情简介(ALL)
            # if(len(response.selector.xpath("//div[@class='indent']/span")) > 2):
            #             #     reportList = response.selector.xpath("//div[@class='indent']/span")[len(response.selector.xpath("//div[@class='indent']/span")) - 2].xpath("./text()").extract()
            report = ''.join(response.selector.xpath("//span[@property='v:summary']/text()").extract())
            movieDetail['report'] = report

            # 推荐(ALL)
            recommendTagList = response.selector.xpath("//div[@class='recommendations-bd']/dl/dd/a")
            recommendList = []
            for recommendTag in recommendTagList:
                recommend = {}
                recommend['id'] = ''.join(recommendTag.xpath('./attribute::href').extract()).replace(
                    'https://movie.douban.com/subject/', '').replace('/?from=subject-page', '')
                recommend['name'] = ''.join(recommendTag.xpath('./text()').extract())
                recommendList.append(recommend)
            movieDetail['recommendList'] = recommendList
            print("影片Detail")
            SaveData().save_media_detail(movieDetail)
            SaveData().save_media_recommend(recommendList, response.meta['id'], response.meta['title'])
            if len(directorList) > 0:
                SaveData().save_media_attr(directorList, response.meta['id'], response.meta['title'], "DIRECTOR")
            if len(writerList) > 0:
                SaveData().save_media_attr(writerList, response.meta['id'], response.meta['title'], "WRITER")
            if len(performerList) > 0:
                SaveData().save_media_attr(performerList, response.meta['id'], response.meta['title'], "PERFORMER")
            SaveData().update_media_history(self.type)

            mediaDataList = SaveData().query_media_data(response.meta['history'], 1)[0]
            if len(mediaDataList) > 0:
                dataItem = mediaDataList
                yield Request(dataItem[4],
                              meta={'classify': dataItem[5], 'id': str(dataItem[1]), 'title': dataItem[2],
                                    'history': response.meta['history'] + 1},
                              callback=self.parse_movie_detail)
        elif response.status == 404:
            SaveData().update_media_history(self.type)
            mediaDataList = SaveData().query_media_data(response.meta['history'], 1)[0]
            if len(mediaDataList) > 0:
                dataItem = mediaDataList
                yield Request(dataItem[4],
                              meta={'classify': dataItem[5], 'id': str(dataItem[1]), 'title': dataItem[2],
                                    'history': response.meta['history'] + 1},
                              callback=self.parse_movie_detail)
        elif response.status == 301 or response.status == 302:
            SaveData().update_media_history(self.type)
            time.sleep(10)
            mediaDataList = SaveData().query_media_data(response.meta['history'], 1)[0]
            if len(mediaDataList) > 0:
                dataItem = mediaDataList
                yield Request(dataItem[4],
                              meta={'classify': dataItem[5], 'id': str(dataItem[1]), 'title': dataItem[2],
                                    'history': response.meta['history'] + 1},
                              callback=self.parse_movie_detail)
