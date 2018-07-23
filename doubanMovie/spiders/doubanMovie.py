from scrapy.spiders import Spider
from scrapy.selector import Selector
from doubanMovie.items import DoubanMovieItem


class DoubanMovieTop250Spider(Spider):
    name = 'douban'
    start_urls = ['https://movie.douban.com/tag/']

    def parse(self, response):
        #print(response.body)
        item = DoubanMovieItem()
        selector = Selector(response)
        #print(selector)
        tags = selector.xpath('//div[@class="tags"]')
        print(tags)
