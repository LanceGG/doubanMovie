from scrapy.spiders import Spider
from scrapy import Request
from scrapy.selector import Selector
from doubanMovie.items import DoubanMovieItem


class DoubanMovie(Spider):
    name = 'douban'
    headers = {
        'Accept': 'application/json, text/plain, */*',
        'Accept-Encoding': 'gzip, deflate, br',
        'Accept-Language': 'zh-CN,zh;q=0.9',
        'Connection': 'keep-alive',
        'host': 'movie.douban.com',
        'Referer': 'https://movie.douban.com/tag/',
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/67.0.3396.99 Safari/537.36',
        'Cookie': 'bid=U96JfASK_Wc; _pk_ses.100001.4cf6=*; __utma=30149280.1122136196.1532341520.1532341520.1532341520.1; __utmb=30149280.0.10.1532341520; __utmc=30149280; __utmz=30149280.1532341520.1.1.utmcsr=(direct)|utmccn=(direct)|utmcmd=(none); __utma=223695111.134179281.1532341520.1532341520.1532341520.1; __utmb=223695111.0.10.1532341520; __utmc=223695111; __utmz=223695111.1532341520.1.1.utmcsr=(direct)|utmccn=(direct)|utmcmd=(none); __yadk_uid=FN0E9MQ2ITxNOmIywZhwODo2uK8PLLU5; ap=1; ct=y; ll="118282"; _vwo_uuid_v2=DC76AA880CDB3905CF9F1836C935C5EC2|03db08648649e8cd3fa0145b2428f48a; _pk_id.100001.4cf6=2864ef4f94aaf12f.1532341520.1.1532342912.1532341520.'
    }

    tags = ["%E7%94%B5%E5%BD%B1", "%E7%94%B5%E8%A7%86%E5%89%A7", "%E7%BB%BC%E8%89%BA", "%E5%8A%A8%E7%94%BB", "%E7%BA%AA%E5%BD%95%E7%89%87", "%E7%9F%AD%E7%89%87"]
    tagNum = 0
    baseUrl = 'https://movie.douban.com/j/new_search_subjects?sort=T&range=0,10&tags={}&start={}'

    def start_requests(self):
        url = self.get_url(0)
        yield Request(url, headers=self.headers)

    def get_url(self, num):
        return str(self.baseUrl.format(self.tags[self.tagNum], num))

    def parse(self, response):
        if 200 == response.status:
            print (response.body)
            pass
