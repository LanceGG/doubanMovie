# -*- coding: utf-8 -*-

# Scrapy settings for doubanMovie project
#
# For simplicity, this file contains only settings considered important or
# commonly used. You can find more settings consulting the documentation:
#
#     https://doc.scrapy.org/en/latest/topics/settings.html
#     https://doc.scrapy.org/en/latest/topics/downloader-middleware.html
#     https://doc.scrapy.org/en/latest/topics/spider-middleware.html

BOT_NAME = 'doubanMovie'

SPIDER_MODULES = ['doubanMovie.spiders']
NEWSPIDER_MODULE = 'doubanMovie.spiders'
COOKIES_ENABLED = False
AUTOTHROTTLE_ENABLED = True
DOWNLOAD_DELAY = 3
DEFAULT_REQUEST_HEADERS = {
    'Accept': 'application/json, text/plain, */*',
    'Accept-Encoding': 'gzip, deflate, br',
    'Accept-Language': 'zh-CN,zh;q=0.9',
    'Connection': 'keep-alive',
    'host': 'movie.douban.com',
    'Referer': 'https://movie.douban.com/tag/',
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/67.0.3396.99 Safari/537.36',
    'Cookie': 'bid=U96JfASK_Wc; __utmc=30149280; __utmc=223695111; __yadk_uid=FN0E9MQ2ITxNOmIywZhwODo2uK8PLLU5; ap=1; ct=y; ll="118282"; _vwo_uuid_v2=DC76AA880CDB3905CF9F1836C935C5EC2|03db08648649e8cd3fa0145b2428f48a; ps=y; push_noty_num=0; push_doumail_num=0; __utmv=30149280.6257; douban-fav-remind=1; __utmz=30149280.1532566392.19.2.utmcsr=baidu|utmccn=(organic)|utmcmd=organic; __utma=30149280.1122136196.1532341520.1532594890.1532603362.27; douban-profile-remind=1; __utmb=30149280.12.10.1532603362; _pk_ref.100001.4cf6=%5B%22%22%2C%22%22%2C1532603813%2C%22https%3A%2F%2Fwww.douban.com%2Fpeople%2F62576053%2F%22%5D; _pk_ses.100001.4cf6=*; __utma=223695111.134179281.1532341520.1532594890.1532603813.24; __utmb=223695111.0.10.1532603813; __utmz=223695111.1532603813.24.2.utmcsr=douban.com|utmccn=(referral)|utmcmd=referral|utmcct=/people/62576053/; _pk_id.100001.4cf6=2864ef4f94aaf12f.1532341520.22.1532603841.1532591523.; dbcl2="62576053:RSDXlqtX+gk"; ck=XgYF'
}
IPPOOL = [
    '27.209.5.55:17255',
    '175.4.20.162:14075',
    '113.110.47.215:16957',
    '112.194.217.118:38176',
    '122.7.226.41:16155',
    '112.194.222.143:10620',
    '220.186.158.86:17102',
    '223.150.38.155:13016',
    '115.51.109.103:15173',
    '122.189.87.57:10877',
]
# USER_AGENT = 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/67.0.3396.99 Safari/537.36'
# USER_AGENT_LIST = [
#     'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/535.7 (KHTML, like Gecko) Chrome/16.0.912.36 Safari/535.7',
#     'Mozilla/5.0 (Windows NT 6.2; Win64; x64; rv:16.0) Gecko/16.0 Firefox/16.0',
#     'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_7_3) AppleWebKit/534.55.3 (KHTML, like Gecko) Version/5.1.3 Safari/534.53.10'
# ]

# USER_AGENT_LIST = [
#     "Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.1 "
#     "(KHTML, like Gecko) Chrome/22.0.1207.1 Safari/537.1",
#     "Mozilla/5.0 (X11; CrOS i686 2268.111.0) AppleWebKit/536.11 "
#     "(KHTML, like Gecko) Chrome/20.0.1132.57 Safari/536.11",
#     "Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/536.6 "
#     "(KHTML, like Gecko) Chrome/20.0.1092.0 Safari/536.6",
#     "Mozilla/5.0 (Windows NT 6.2) AppleWebKit/536.6 "
#     "(KHTML, like Gecko) Chrome/20.0.1090.0 Safari/536.6",
#     "Mozilla/5.0 (Windows NT 6.2; WOW64) AppleWebKit/537.1 "
#     "(KHTML, like Gecko) Chrome/19.77.34.5 Safari/537.1",
#     "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/536.5 "
#     "(KHTML, like Gecko) Chrome/19.0.1084.9 Safari/536.5",
#     "Mozilla/5.0 (Windows NT 6.0) AppleWebKit/536.5 "
#     "(KHTML, like Gecko) Chrome/19.0.1084.36 Safari/536.5",
#     "Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/536.3 "
#     "(KHTML, like Gecko) Chrome/19.0.1063.0 Safari/536.3",
#     "Mozilla/5.0 (Windows NT 5.1) AppleWebKit/536.3 "
#     "(KHTML, like Gecko) Chrome/19.0.1063.0 Safari/536.3",
#     "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_8_0) AppleWebKit/536.3 "
#     "(KHTML, like Gecko) Chrome/19.0.1063.0 Safari/536.3",
#     "Mozilla/5.0 (Windows NT 6.2) AppleWebKit/536.3 "
#     "(KHTML, like Gecko) Chrome/19.0.1062.0 Safari/536.3",
#     "Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/536.3 "
#     "(KHTML, like Gecko) Chrome/19.0.1062.0 Safari/536.3",
#     "Mozilla/5.0 (Windows NT 6.2) AppleWebKit/536.3 "
#     "(KHTML, like Gecko) Chrome/19.0.1061.1 Safari/536.3",
#     "Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/536.3 "
#     "(KHTML, like Gecko) Chrome/19.0.1061.1 Safari/536.3",
#     "Mozilla/5.0 (Windows NT 6.1) AppleWebKit/536.3 "
#     "(KHTML, like Gecko) Chrome/19.0.1061.1 Safari/536.3",
#     "Mozilla/5.0 (Windows NT 6.2) AppleWebKit/536.3 "
#     "(KHTML, like Gecko) Chrome/19.0.1061.0 Safari/536.3",
#     "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/535.24 "
#     "(KHTML, like Gecko) Chrome/19.0.1055.1 Safari/535.24",
#     "Mozilla/5.0 (Windows NT 6.2; WOW64) AppleWebKit/535.24 "
#     "(KHTML, like Gecko) Chrome/19.0.1055.1 Safari/535.24"
# ]

HTTP_PROXY = 'http://180.102.149.199:17563'
DOWNLOADER_MIDDLEWARES = {
    'doubanMovie.middlewares.DoubanmovieDownloaderMiddleware': 400,
    'doubanMovie.middlewares.DoubanmovieSpiderMiddleware': 410,
    # 'scrapy.downloadermiddlewares.useragent.UserAgentMiddleware': None
    # Disable compression middleware, so the actual HTML pages are cached
}
HTTPERROR_ALLOWED_CODES = [403,  404, 301, 302]
# Crawl responsibly by identifying yourself (and your website) on the user-agent
# USER_AGENT = 'doubanMovie (+http://www.yourdomain.com)'

# Obey robots.txt rules
ROBOTSTXT_OBEY = False

# Configure maximum concurrent requests performed by Scrapy (default: 16) 并发请求数
CONCURRENT_REQUESTS = 16

# Configure a delay for requests for the same website (default: 0)
# See https://doc.scrapy.org/en/latest/topics/settings.html#download-delay
# See also autothrottle settings and docs
DOWNLOAD_DELAY = 3
# The download delay setting will honor only one of:
# CONCURRENT_REQUESTS_PER_DOMAIN = 16
# CONCURRENT_REQUESTS_PER_IP = 16

# Disable cookies (enabled by default)
# COOKIES_ENABLED = False

# Disable Telnet Console (enabled by default)
# TELNETCONSOLE_ENABLED = False

# Override the default request headers:
# DEFAULT_REQUEST_HEADERS = {
#   'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8',
#   'Accept-Language': 'en',
# }

# Enable or disable spider middlewares
# See https://doc.scrapy.org/en/latest/topics/spider-middleware.html
# SPIDER_MIDDLEWARES = {
#    'doubanMovie.middlewares.DoubanmovieSpiderMiddleware': 543,
# }

# Enable or disable downloader middlewares
# See https://doc.scrapy.org/en/latest/topics/downloader-middleware.html
# DOWNLOADER_MIDDLEWARES = {
#    'doubanMovie.middlewares.DoubanmovieDownloaderMiddleware': 543,
# }

# Enable or disable extensions
# See https://doc.scrapy.org/en/latest/topics/extensions.html
# EXTENSIONS = {
#    'scrapy.extensions.telnet.TelnetConsole': None,
# }

# Configure item pipelines
# See https://doc.scrapy.org/en/latest/topics/item-pipeline.html
ITEM_PIPELINES = {
    'doubanMovie.pipelines.DoubanmoviePipeline': 1,
    'doubanMovie.pipelines.MyImagesPipeline':1
}
IMAGES_URLS_FIELD = 'url'
IMAGES_STORE = r'.'

# Enable and configure the AutoThrottle extension (disabled by default)
# See https://doc.scrapy.org/en/latest/topics/autothrottle.html
# AUTOTHROTTLE_ENABLED = True
# The initial download delay
# AUTOTHROTTLE_START_DELAY = 5
# The maximum download delay to be set in case of high latencies
# AUTOTHROTTLE_MAX_DELAY = 60
# The average number of requests Scrapy should be sending in parallel to
# each remote server
# AUTOTHROTTLE_TARGET_CONCURRENCY = 1.0
# Enable showing throttling stats for every response received:
# AUTOTHROTTLE_DEBUG = False

# Enable and configure HTTP caching (disabled by default)
# See https://doc.scrapy.org/en/latest/topics/downloader-middleware.html#httpcache-middleware-settings
# HTTPCACHE_ENABLED = True
# HTTPCACHE_EXPIRATION_SECS = 0
# HTTPCACHE_DIR = 'httpcache'
# HTTPCACHE_IGNORE_HTTP_CODES = []
# HTTPCACHE_STORAGE = 'scrapy.extensions.httpcache.FilesystemCacheStorage'
