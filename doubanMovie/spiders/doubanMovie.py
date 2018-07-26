# -*- coding: utf-8 -*-
from scrapy.spiders import Spider
from scrapy import Request
import urllib.parse
import json
import os
from scrapy.selector import Selector
from doubanMovie.items import DoubanMovieItem
from doubanMovie.spiders.SaveData import SaveData


class DoubanMovie(Spider):
    name = 'doubanMovie'
    headers = {
        'Accept': 'application/json, text/plain, */*',
        'Accept-Encoding': 'gzip, deflate, br',
        'Accept-Language': 'zh-CN,zh;q=0.9',
        'Connection': 'keep-alive',
        'host': 'movie.douban.com',
        'Referer': 'https://movie.douban.com/tag/',
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/67.0.3396.99 Safari/537.36',
         'Cookie': 'bid=U96JfASK_Wc; __utmc=30149280; __utmz=30149280.1532341520.1.1.utmcsr=(direct)|utmccn=(direct)|utmcmd=(none); __utmc=223695111; __utmz=223695111.1532341520.1.1.utmcsr=(direct)|utmccn=(direct)|utmcmd=(none); __yadk_uid=FN0E9MQ2ITxNOmIywZhwODo2uK8PLLU5; ap=1; ct=y; ll="118282"; _vwo_uuid_v2=DC76AA880CDB3905CF9F1836C935C5EC2|03db08648649e8cd3fa0145b2428f48a; _pk_ses.100001.4cf6=*; __utma=30149280.1122136196.1532341520.1532393838.1532397873.4; __utmb=30149280.0.10.1532397873; __utma=223695111.134179281.1532341520.1532393838.1532397873.4; __utmb=223695111.0.10.1532397873; ps=y; dbcl2="62576053:8HYw7Qs7p0U"; ck=_RjC; push_noty_num=0; push_doumail_num=0; _pk_id.100001.4cf6=2864ef4f94aaf12f.1532341520.4.1532399007.1532396026.'
    }

    # 电影
    movieList = []
    # 电影详情
    movieDetailList = []
    # 获奖详情
    movieAwardList = []
    # 演员
    actorList = []
    actorIdList = []
    # pic
    moviePicIds = []
    picNum = 0
    movieId = 0
    moviePic = {}
    # 分类
    tags = ["电影", "电视剧", "综艺", "动画", "纪录片", "短片"]
    tagNum = 0
    num = 0

    baseUrl = 'https://movie.douban.com/j/new_search_subjects?sort=T&range=0,10&tags={}&start={}'
    picUrl = 'https://movie.douban.com/subject/{}/photos?type=R&start={}&sortby=like&size=a&subtype=a'

    def start_requests(self):
        history = SaveData().query_history_data()
        self.tagNum = history[0][0]
        self.num = history[0][1]
        url = self.get_url()
        yield Request(url, callback=self.parse)

    def get_url(self):
        return str(self.baseUrl.format(urllib.parse.quote(self.tags[self.tagNum]), self.num))

    def parse(self, response):
        data = json.loads(response.body.decode('utf-8'))['data']
        for movieItem in data:
            movieItem['classify'] = self.tags[self.tagNum]
        print("影片Outer")
        print(data)
        SaveData().save_media_data(data)
        SaveData().save_history_data(self.tagNum, self.num)

        # # 遍历循环, 爬电影, 电视剧, 综艺, 动画, 纪录片, 短片
        # if len(data) != 0:
        #     self.num += 20
        #     url = self.get_url()
        #     yield Request(url, callback=self.parse)
        # else:
        #     if self.tagNum < 5:
        #         self.tagNum += 1
        #         self.num = 0
        #         url = self.get_url()
        #         yield Request(url, callback=self.parse)

    # # 保存查到的影片的基础数据
    # movieFile = './movie/movie.json'
    # with open(movieFile, 'w') as f:
    #     json.dump(self.movieList, f)
    #
    # # 查找影片详情数据
    # for dataItem in self.movieList:
    #     # 影片详情
    #     detailUrl = dataItem['url']
    #     yield Request(detailUrl, headers=self.headers, meta={'classify': dataItem['classify'], 'id': dataItem['id']}, callback=self.parse_movie_detail)
    # movieDetailFile = './movie/movieDetail.json'
    # with open(movieDetailFile, 'w') as f:
    #     json.dump(self.movieDetailList, f)
    #
    # # 查找影片的获奖情况
    # for dataItem in self.movieList:
    #     # 影片奖励详情
    #     awardUrl = dataItem['url'] + 'awards/'
    #     yield Request(awardUrl, headers=self.headers, callback=self.parse_movie_rewards)
    # movieAwardFile = './movie/movieAward.json'
    # with open(movieAwardFile, 'w') as f:
    #     json.dump(self.movieAwardList, f)
    #
    # # 演员详情
    # for actorId in self.actorIdList:
    #     url = 'https://movie.douban.com/celebrity/' + str(actorId) + '/'
    #     yield Request(url, headers=self.headers, callback=self.parse_actor_detail)
    # actorFile = './movie/movieAward.json'
    # with open(actorFile, 'w') as f:
    #     json.dump(self.movieList, f)
    #
    # # 查找影片的相关图片id
    # for dataItem in self.movieList:
    #     # 影片相关图片
    #     self.moviePicIds = []
    #     picUrl = self.get_pic_url(dataItem['id'], 0)
    #     yield Request(picUrl, headers=self.headers, meta={'movieId': dataItem['id'], 'picNum': 0, 'moviePicIds': []}, callback=self.parse_movie_pic)

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
                director['id'] = ''.join(directorTag.xpath('./attribute::href').extract()).replace('/celebrity/',
                                                                                                   '').replace('/', '')
                director['name'] = ''.join(directorTag.xpath('./text()').extract())
                directorList.append(director)
                self.get_actor_by_id(director['id'])
            movieDetail['directorList'] = directorList

            # 编剧(ALL)
            writerTagList = response.selector.xpath("//span[contains(text(),'编剧')]/../span[@class='attrs']/a")
            writerList = []
            for writerTag in writerTagList:
                writer = {}
                writer['id'] = ''.join(writerTag.xpath('./attribute::href').extract()).replace('/celebrity/',
                                                                                               '').replace('/', '')
                writer['name'] = ''.join(writerTag.xpath('./text()').extract())
                writerList.append(writer)
                self.get_actor_by_id(writer['id'])
            movieDetail['writerList'] = writerList

            # 主演(ALL)
            performerTagList = response.selector.xpath("//span[contains(text(),'主演')]/../span[@class='attrs']/a")
            performerList = []
            for performerTag in performerTagList:
                performer = {}
                performer['id'] = ''.join(performerTag.xpath('./attribute::href').extract()).replace('/celebrity/',
                                                                                                     '').replace('/',
                                                                                                                 '')
                performer['name'] = ''.join(performerTag.xpath('./text()').extract())
                performerList.append(performer)
                self.get_actor_by_id(performer['id'])
            movieDetail['performerList'] = performerList

            # 类型(ALL)
            typeList = response.selector.xpath("//span[@property='v:genre']/text()").extract()
            movieDetail['typeList'] = typeList

            # 制片国家/地区(ALL)
            country = ''.join(
                response.selector.xpath("//span[contains(text(), '制片国家/地区')]/following::text()[1]").extract())
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
                season = ''.join(
                    response.selector.xpath("//select[@id='season']/option[@selected='selected']/text()").extract())
                movieDetail['season'] = season

            # 集数(MULTI)
            if self.tagNum in [1, 2]:
                episodes = ''.join(
                    response.selector.xpath("//span[contains(text(), '集数')]/following::text()[1]").extract()).replace(
                    ' ', '').replace('\n', '')
                movieDetail['episodes'] = episodes

            # 单集片长(MULTI)
            if self.tagNum in [1, 2]:
                alongRuntime = ''.join(
                    response.selector.xpath("//span[contains(text(), '单集片长')]/following::text()[1]").extract())
                movieDetail['alongRuntime'] = alongRuntime

            # 又名(ALL)
            alias = ''.join(response.selector.xpath("//span[contains(text(), '又名')]/following::text()[1]").extract())
            movieDetail['alias'] = alias

            # IMDbId(ALL)
            IMDbId = ''.join(
                response.selector.xpath("//span[contains(text(), 'IMDb链接')]/following::a[1]/text()").extract())
            movieDetail['IMDbId'] = IMDbId

            # 评分(ALL)
            score = ''.join(response.selector.xpath("//strong[@class='ll rating_num']/text()").extract())
            movieDetail['score'] = score

            # 评分等级(ALL)
            rating = {}
            rating['stars5'] = ''.join(response.selector.xpath(
                "//span[@class='stars5 starstop']/../span[@class='rating_per']/text()").extract())
            rating['stars4'] = ''.join(response.selector.xpath(
                "//span[@class='stars4 starstop']/../span[@class='rating_per']/text()").extract())
            rating['stars3'] = ''.join(response.selector.xpath(
                "//span[@class='stars3 starstop']/../span[@class='rating_per']/text()").extract())
            rating['stars2'] = ''.join(response.selector.xpath(
                "//span[@class='stars2 starstop']/../span[@class='rating_per']/text()").extract())
            rating['stars1'] = ''.join(response.selector.xpath(
                "//span[@class='stars1 starstop']/../span[@class='rating_per']/text()").extract())
            rating['peopleNum'] = ''.join(response.selector.xpath("//span[@property='v:votes']/text()").extract())
            movieDetail['rating'] = rating

            # 标签(ALL)
            tags = response.selector.xpath("//div[@class='tags-body']/a/text()").extract()
            movieDetail['tags'] = tags

            # 剧情简介(ALL)
            report = ''
            reportList = response.selector.xpath("//div[@class='indent']/span")[
                len(response.selector.xpath("//div[@class='indent']/span")) - 2].xpath("./text()").extract()
            movieDetail['report'] = ''.join(reportList)

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
            print ("影片Detail")
            print (movieDetail)
            self.movieDetailList.append(movieDetail)
        else:
            url = response.url
            print ("影片Detail" + response.status + ": 访问失败, 重新访问")
            yield Request(url, headers=self.headers,
                          meta={'classify': response.meta['classify'], 'id': response.meta['id']},
                          callback=self.parse_movie_detail)

    def parse_movie_rewards(self, response):
        if response.status == 200:
            movieReward = {}
            movieReward['id'] = response.url.replace('https://movie.douban.com/subject/', '').replace('/awards/', '')
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
            self.movieAwardList.append(movieReward)
        else:
            url = response.url
            print ("影片Reward" + response.status + ": 访问失败, 重新访问")
            yield Request(url, headers=self.headers, callback=self.parse_movie_rewards)

    def get_actor_by_id(self, actorId):
        if actorId in self.actorIdList:
            pass
        else:
            self.actorIdList.append(actorId)

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
            self.actorList.append(actor)
        else:
            url = response.url
            print ("演员Detail" + response.status + ": 访问失败, 重新访问")
            yield Request(url, headers=self.headers, callback=self.parse_actor_detail)

    def get_pic_url(self, movieId, picNum):
        return self.picUrl.format(movieId, picNum)

    def parse_movie_pic(self, response):
        if 200 == response.status:
            picIds = response.selector.xpath("//ul[@class='poster-col3 clearfix']/li/attribute::data-id").extract()
            if len(picIds) == 0:
                self.down_movie_pic(response.meta['movieId'], response.meta['moviePicIds'])
                self.moviePic[response.meta['movieId']] = response.meta['moviePicIds']
            else:
                print("图片id")
                print(picIds)
                moviePicIds = response.meta['moviePicIds'] + picIds
                picNum = response.meta['picNum'] + 30
                url = self.get_pic_url(response.meta['movieId'], picNum)
                yield Request(url, headers=self.headers,
                              meta={'movieId': response.meta['movieId'], 'picNum': picNum, 'moviePicIds': moviePicIds},
                              callback=self.parse_movie_pic)

    # 下载影片
    def down_movie_pic(self, movieId, moviePicIds):
        item = DoubanMovieItem()
        item['movieId'] = movieId
        item['moviePicIds'] = moviePicIds
        yield item
