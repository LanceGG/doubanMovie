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
USER_AGENT = 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/67.0.3396.99 Safari/537.36'
# COOKIE = 'bid=U96JfASK_Wc; _pk_ses.100001.4cf6=*; __utma=30149280.1122136196.1532341520.1532341520.1532341520.1; __utmb=30149280.0.10.1532341520; __utmc=30149280; __utmz=30149280.1532341520.1.1.utmcsr=(direct)|utmccn=(direct)|utmcmd=(none); __utma=223695111.134179281.1532341520.1532341520.1532341520.1; __utmb=223695111.0.10.1532341520; __utmc=223695111; __utmz=223695111.1532341520.1.1.utmcsr=(direct)|utmccn=(direct)|utmcmd=(none); __yadk_uid=FN0E9MQ2ITxNOmIywZhwODo2uK8PLLU5; ap=1; ct=y; ll="118282"; _vwo_uuid_v2=DC76AA880CDB3905CF9F1836C935C5EC2|03db08648649e8cd3fa0145b2428f48a; _pk_id.100001.4cf6=2864ef4f94aaf12f.1532341520.1.1532342912.1532341520.'
# REFER = 'https://movie.douban.com/tag/'
# DEFAULT_REQUEST_HEADERS = {
#     'Accept': 'application/json, text/plain, */*',
#     'Accept-Encoding':  'gzip, deflate, br',
#     'Accept-Language': 'zh-CN,zh;q=0.9',
#     'Connection':  'keep-alive',
#     'host': 'movie.douban.com',
#     'Referer': 'https://movie.douban.com/tag/',
#     'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/67.0.3396.99 Safari/537.36',
#     'Cookie': 'bid=U96JfASK_Wc; _pk_ses.100001.4cf6=*; __utma=30149280.1122136196.1532341520.1532341520.1532341520.1; __utmb=30149280.0.10.1532341520; __utmc=30149280; __utmz=30149280.1532341520.1.1.utmcsr=(direct)|utmccn=(direct)|utmcmd=(none); __utma=223695111.134179281.1532341520.1532341520.1532341520.1; __utmb=223695111.0.10.1532341520; __utmc=223695111; __utmz=223695111.1532341520.1.1.utmcsr=(direct)|utmccn=(direct)|utmcmd=(none); __yadk_uid=FN0E9MQ2ITxNOmIywZhwODo2uK8PLLU5; ap=1; ct=y; ll="118282"; _vwo_uuid_v2=DC76AA880CDB3905CF9F1836C935C5EC2|03db08648649e8cd3fa0145b2428f48a; _pk_id.100001.4cf6=2864ef4f94aaf12f.1532341520.1.1532342912.1532341520.'
# }

# Crawl responsibly by identifying yourself (and your website) on the user-agent
#USER_AGENT = 'doubanMovie (+http://www.yourdomain.com)'

# Obey robots.txt rules
ROBOTSTXT_OBEY = False

# Configure maximum concurrent requests performed by Scrapy (default: 16)
#CONCURRENT_REQUESTS = 32

# Configure a delay for requests for the same website (default: 0)
# See https://doc.scrapy.org/en/latest/topics/settings.html#download-delay
# See also autothrottle settings and docs
#DOWNLOAD_DELAY = 3
# The download delay setting will honor only one of:
#CONCURRENT_REQUESTS_PER_DOMAIN = 16
#CONCURRENT_REQUESTS_PER_IP = 16

# Disable cookies (enabled by default)
#COOKIES_ENABLED = False

# Disable Telnet Console (enabled by default)
#TELNETCONSOLE_ENABLED = False

# Override the default request headers:
#DEFAULT_REQUEST_HEADERS = {
#   'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8',
#   'Accept-Language': 'en',
#}

# Enable or disable spider middlewares
# See https://doc.scrapy.org/en/latest/topics/spider-middleware.html
#SPIDER_MIDDLEWARES = {
#    'doubanMovie.middlewares.DoubanmovieSpiderMiddleware': 543,
#}

# Enable or disable downloader middlewares
# See https://doc.scrapy.org/en/latest/topics/downloader-middleware.html
#DOWNLOADER_MIDDLEWARES = {
#    'doubanMovie.middlewares.DoubanmovieDownloaderMiddleware': 543,
#}

# Enable or disable extensions
# See https://doc.scrapy.org/en/latest/topics/extensions.html
#EXTENSIONS = {
#    'scrapy.extensions.telnet.TelnetConsole': None,
#}

# Configure item pipelines
# See https://doc.scrapy.org/en/latest/topics/item-pipeline.html
#ITEM_PIPELINES = {
#    'doubanMovie.pipelines.DoubanmoviePipeline': 300,
#}

# Enable and configure the AutoThrottle extension (disabled by default)
# See https://doc.scrapy.org/en/latest/topics/autothrottle.html
#AUTOTHROTTLE_ENABLED = True
# The initial download delay
#AUTOTHROTTLE_START_DELAY = 5
# The maximum download delay to be set in case of high latencies
#AUTOTHROTTLE_MAX_DELAY = 60
# The average number of requests Scrapy should be sending in parallel to
# each remote server
#AUTOTHROTTLE_TARGET_CONCURRENCY = 1.0
# Enable showing throttling stats for every response received:
#AUTOTHROTTLE_DEBUG = False

# Enable and configure HTTP caching (disabled by default)
# See https://doc.scrapy.org/en/latest/topics/downloader-middleware.html#httpcache-middleware-settings
#HTTPCACHE_ENABLED = True
#HTTPCACHE_EXPIRATION_SECS = 0
#HTTPCACHE_DIR = 'httpcache'
#HTTPCACHE_IGNORE_HTTP_CODES = []
#HTTPCACHE_STORAGE = 'scrapy.extensions.httpcache.FilesystemCacheStorage'
