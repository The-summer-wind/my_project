# -*- coding: utf-8 -*-

# Scrapy settings for Home project
#
# For simplicity, this file contains only settings considered important or
# commonly used. You can find more settings consulting the documentation:
#
#     https://docs.scrapy.org/en/latest/topics/settings.html
#     https://docs.scrapy.org/en/latest/topics/downloader-middleware.html
#     https://docs.scrapy.org/en/latest/topics/spider-middleware.html

BOT_NAME = 'Home'

SPIDER_MODULES = ['Home.spiders']
NEWSPIDER_MODULE = 'Home.spiders'


# Crawl responsibly by identifying yourself (and your website) on the user-agent
#USER_AGENT = 'Home (+http://www.yourdomain.com)'

# Obey robots.txt rules
ROBOTSTXT_OBEY = False

# Configure maximum concurrent requests performed by Scrapy (default: 16)
#CONCURRENT_REQUESTS = 32

# Configure a delay for requests for the same website (default: 0)
# See https://docs.scrapy.org/en/latest/topics/settings.html#download-delay
# See also autothrottle settings and docs
DOWNLOAD_DELAY = 1
# The download delay setting will honor only one of:
#CONCURRENT_REQUESTS_PER_DOMAIN = 16
#CONCURRENT_REQUESTS_PER_IP = 16

# Disable cookies (enabled by default)
COOKIES_ENABLED = False

# Disable Telnet Console (enabled by default)
#TELNETCONSOLE_ENABLED = False

# Override the default request headers:
DEFAULT_REQUEST_HEADERS = {
  'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8',
  'Accept-Language': 'en',
  'Cookie': 'f=n; time_create=1596446821253; userid360_xml=6FB7E4BB266300F77F710D6275675FC0; id58=c5/nfF8AS2ComqtzILrnAg==; wmda_uuid=e2cc0ad10014800eacd5990f19a90f95; wmda_new_uuid=1; wmda_visited_projects=%3B11187958619315; 58tj_uuid=21a24e94-031a-42f7-ba64-6ff9579600ca; als=0; f=n; xxzl_deviceid=1Ixdcz2GcRxb31LqnyU6fNrLg1ymzR%2Ff3k75aU1lhQIMSXmEB16SAT52jRQeledl; xzfzqtoken=2pAGowlOY9SwlH3rum0nBXeHNUVlKiXkPalUJ1RXGGce15rBq1LPgQ1FLmZzlWBMin35brBb%2F%2FeSODvMgkQULA%3D%3D; xxzl_cid=64bb595ca3e54101bae3f50c0984d8c9; xzuid=1cd70925-a9fb-43b8-b4ad-8eaed5539d53; new_session=1; new_uv=3; utm_source=; spm=; init_refer=https%253A%252F%252Fcq.58.com%252Fchuzu%252Fpn40%252F; ppStore_fingerprint=2A1C578CAAC583EBE0AC35133764811CEFAFF4DAE8CF1A49%EF%BC%BF1593934966252; wmda_session_id_11187958619315=1593934968210-eca95444-5475-0edd',
  'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/83.0.4103.97 Safari/537.36'
}

# Enable or disable spider middlewares
# See https://docs.scrapy.org/en/latest/topics/spider-middleware.html
#SPIDER_MIDDLEWARES = {
#    'Home.middlewares.HomeSpiderMiddleware': 543,
#}

# Enable or disable downloader middlewares
# See https://docs.scrapy.org/en/latest/topics/downloader-middleware.html
#DOWNLOADER_MIDDLEWARES = {
#    'Home.middlewares.HomeDownloaderMiddleware': 543,
#}

# Enable or disable extensions
# See https://docs.scrapy.org/en/latest/topics/extensions.html
#EXTENSIONS = {
#    'scrapy.extensions.telnet.TelnetConsole': None,
#}

# Configure item pipelines
# See https://docs.scrapy.org/en/latest/topics/item-pipeline.html
ITEM_PIPELINES = {
   'Home.pipelines.HomePipeline': 300,
   'Home.pipelines.HomeMysqlPipeline':400,
   # 'Home.pipelines.HomeMongopipeline':500,
}

# Enable and configure the AutoThrottle extension (disabled by default)
# See https://docs.scrapy.org/en/latest/topics/autothrottle.html
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
# See https://docs.scrapy.org/en/latest/topics/downloader-middleware.html#httpcache-middleware-settings
#HTTPCACHE_ENABLED = True
#HTTPCACHE_EXPIRATION_SECS = 0
#HTTPCACHE_DIR = 'httpcache'
#HTTPCACHE_IGNORE_HTTP_CODES = []
#HTTPCACHE_STORAGE = 'scrapy.extensions.httpcache.FilesystemCacheStorage'

# MONGO_HOST = 'localhost'
# MONGO_PORT = '27017'
# MONGO_DB = 'homedb'
# MONGO_SET = 'homeset'
MYSQL_HOST = 'localhost'
MYSQL_USER = 'root'
MYSQL_PWD = '123456'
MYSQL_DB = 'homedb'
CHARSET = 'utf8'