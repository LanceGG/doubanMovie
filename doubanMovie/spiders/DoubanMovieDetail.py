# -*- coding: utf-8 -*-
from scrapy.spiders import Spider
from scrapy import Request
import urllib.parse
from doubanMovie.spiders.SaveData import SaveData


class DoubanMovieDetail(Spider):
    # for dataItem in self.movieList:
    #     # 影片详情
    #     detailUrl = dataItem['url']
    #     yield Request(detailUrl, headers=self.headers, meta={'classify': dataItem['classify'], 'id': dataItem['id']}, callback=self.parse_movie_detail)
    pass

    def parse_movie_detail(self, response):
        if 200 == response.status:
            movieDetail = {}
            # ID(ALL)
            id = response.meta['id']
            movieDetail['id'] = id

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
                director['id'] = ''.join(directorTag.xpath('./attribute::href').extract()).replace('/celebrity/', '').replace('/', '')
                director['name'] = ''.join(directorTag.xpath('./text()').extract())
                directorList.append(director)
                self.get_actor_by_id(director['id'])
            movieDetail['directorList'] = directorList

            # 编剧(ALL)
            writerTagList = response.selector.xpath("//span[contains(text(),'编剧')]/../span[@class='attrs']/a")
            writerList = []
            for writerTag in writerTagList:
                writer = {}
                writer['id'] = ''.join(writerTag.xpath('./attribute::href').extract()).replace('/celebrity/', '').replace('/', '')
                writer['name'] = ''.join(writerTag.xpath('./text()').extract())
                writerList.append(writer)
                self.get_actor_by_id(writer['id'])
            movieDetail['writerList'] = writerList

            # 主演(ALL)
            performerTagList = response.selector.xpath("//span[contains(text(),'主演')]/../span[@class='attrs']/a")
            performerList = []
            for performerTag in performerTagList:
                performer = {}
                performer['id'] = ''.join(performerTag.xpath('./attribute::href').extract()).replace('/celebrity/', '').replace('/', '')
                performer['name'] = ''.join(performerTag.xpath('./text()').extract())
                performerList.append(performer)
                self.get_actor_by_id(performer['id'])
            movieDetail['performerList'] = performerList

            # 类型(ALL)
            typeList = response.selector.xpath("//span[@property='v:genre']/text()").extract()
            movieDetail['typeList'] = typeList

            # 制片国家/地区(ALL)
            country = ''.join(response.selector.xpath("//span[contains(text(), '制片国家/地区')]/following::text()[1]").extract())
            movieDetail['country'] = country

            # 语言(ALL)
            language = ''.join(response.selector.xpath("//span[contains(text(), '语言')]/following::text()[1]").extract())
            movieDetail['language'] = language

            # 上映日期(ALL)
            releaseDates = response.selector.xpath("//span[@property='v:initialReleaseDate']/text()").extract()
            movieDetail['releaseDates'] = releaseDates

            # 片长(ALONG)
            if self.tagNum in [0, 3, 4, 5]:
                runtime = ''.join(response.selector.xpath("//span[@property='v:runtime']/text()").extract())
                movieDetail['runtime'] = runtime

            # 季数(MULTI)
            if self.tagNum in [1, 2]:
                season = ''.join(response.selector.xpath("//select[@id='season']/option[@selected='selected']/text()").extract())
                movieDetail['season'] = season

            # 集数(MULTI)
            if self.tagNum in [1, 2]:
                episodes = ''.join(response.selector.xpath("//span[contains(text(), '集数')]/following::text()[1]").extract()).replace(' ', '').replace('\n', '')
                movieDetail['episodes'] = episodes

            # 单集片长(MULTI)
            if self.tagNum in [1, 2]:
                alongRuntime = ''.join(response.selector.xpath("//span[contains(text(), '单集片长')]/following::text()[1]").extract())
                movieDetail['alongRuntime'] = alongRuntime

            # 又名(ALL)
            alias = ''.join(response.selector.xpath("//span[contains(text(), '又名')]/following::text()[1]").extract())
            movieDetail['alias'] = alias

            # IMDbId(ALL)
            IMDbId = ''.join(response.selector.xpath("//span[contains(text(), 'IMDb链接')]/following::a[1]/text()").extract())
            movieDetail['IMDbId'] = IMDbId

            # 评分(ALL)
            score = ''.join(response.selector.xpath("//strong[@class='ll rating_num']/text()").extract())
            movieDetail['score'] = score

            # 评分等级(ALL)
            rating = {}
            rating['stars5'] = ''.join(response.selector.xpath("//span[@class='stars5 starstop']/../span[@class='rating_per']/text()").extract())
            rating['stars4'] = ''.join(response.selector.xpath("//span[@class='stars4 starstop']/../span[@class='rating_per']/text()").extract())
            rating['stars3'] = ''.join(response.selector.xpath("//span[@class='stars3 starstop']/../span[@class='rating_per']/text()").extract())
            rating['stars2'] = ''.join(response.selector.xpath("//span[@class='stars2 starstop']/../span[@class='rating_per']/text()").extract())
            rating['stars1'] = ''.join(response.selector.xpath("//span[@class='stars1 starstop']/../span[@class='rating_per']/text()").extract())
            rating['peopleNum'] = ''.join(response.selector.xpath("//span[@property='v:votes']/text()").extract())
            movieDetail['rating'] = rating

            # 标签(ALL)
            tags = response.selector.xpath("//div[@class='tags-body']/a/text()").extract()
            movieDetail['tags'] = tags

            # 剧情简介(ALL)
            report = ''
            reportList = response.selector.xpath("//div[@class='indent']/span")[len(response.selector.xpath("//div[@class='indent']/span"))-2].xpath("./text()").extract()
            movieDetail['report'] = ''.join(reportList)

            # 推荐(ALL)
            recommendTagList = response.selector.xpath("//div[@class='recommendations-bd']/dl/dd/a")
            recommendList = []
            for recommendTag in recommendTagList:
                recommend = {}
                recommend['id'] = ''.join(recommendTag.xpath('./attribute::href').extract()).replace('https://movie.douban.com/subject/', '').replace('/?from=subject-page', '')
                recommend['name'] = ''.join(recommendTag.xpath('./text()').extract())
                recommendList.append(recommend)
            movieDetail['recommendList'] = recommendList
            print ("影片Detail")
            print (movieDetail)
            self.movieDetailList.append(movieDetail)
        else:
            url = response.url
            print ("影片Detail" + response.status + ": 访问失败, 重新访问")
            yield Request(url, headers=self.headers,meta={'classify': response.meta['classify'], 'id': response.meta['id']}, callback=self.parse_movie_detail)