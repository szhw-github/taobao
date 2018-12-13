# -*- coding: utf-8 -*-

# Scrapy settings for taobaosearch project
#
# For simplicity, this file contains only settings considered important or
# commonly used. You can find more settings consulting the documentation:
#
#     https://doc.scrapy.org/en/latest/topics/settings.html
#     https://doc.scrapy.org/en/latest/topics/downloader-middleware.html
#     https://doc.scrapy.org/en/latest/topics/spider-middleware.html

BOT_NAME = 'taobaosearch'

SPIDER_MODULES = ['taobaosearch.spiders']
NEWSPIDER_MODULE = 'taobaosearch.spiders'

#my settings starts here
query='优衣库 女装'

START_URL='https://s.taobao.com/search?data-key=s&data-value={datavalue}&ajax=true&q={query}&imgfile=&commend=all&ssid=s5-e&search_type=item&sourceId=tb.index&spm=a21bo.2017.201856-taobao-item.1&ie=utf8&initiative_id=tbindexz_20170306&bcoffset=3&ntoffset=0&p4ppushleft=1%2C48'

HEADERS={
':authority':	's.taobao.com',
'user-agent':	'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/71.0.3578.30 Safari/537.36',
'accept':	'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8',
'referer':	'https://www.taobao.com/',
'accept-encoding':	'gzip, deflate, br',
'accept-language':	'en-US,en;q=0.9'
}
COOKIES={'t': '2b2fa1106028b9a8d764be799f9547f0', ' cna': 'rHN9FKDPCCwCAXtCIyxuXc9d', ' thw': 'cn', ' hng': 'CN%7Czh-CN%7CCNY%7C156', ' tg': '0', ' enc': 'hN7tjQ0fE5%2Bo45tNQyQ1h8YlS9gehvqb3%2F6%2FEQ%2BHUv6u3EDnpDK8zAUzkMhYto7TZ4OFj25mVrUGjnugFIXzwQ%3D%3D', ' x': 'e%3D1%26p%3D*%26s%3D0%26c%3D0%26f%3D0%26g%3D0%26t%3D0%26__ll%3D-1%26_ato%3D0', ' uc3': 'vt3=F8dByR1X72%2FXOPAXtnA%3D&id2=UoncjfNi%2F6tAOw%3D%3D&nk2=2QMT8RXjLe3QJpQ%3D&lg2=Vq8l%2BKCLz3%2F65A%3D%3D', ' tracknick': '%5Cu6D77%5Cu91CC%5Cu9488june6', ' lgc': '%5Cu6D77%5Cu91CC%5Cu9488june6', ' _cc_': 'VFC%2FuZ9ajQ%3D%3D', ' mt': 'ci=-1_0', ' uc1': 'cookie14=UoTYMhjV8bPVSg%3D%3D', ' cookie2': '18c109af567d57eb79ae2bf80dd76944', ' v': '0', ' _tb_token_': '7757661e0537', ' isg': 'BBUVUxT85UT0T8ZegsWODayBJBgPushMjsVmk5e61Qzb7jfgQ2LZ9CPMvOrYbuHc'}
UA='Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/71.0.3578.30 Safari/537.36'
MONGO_URI='mongodb://localhost:27017/'
MONGO_DB='taobao'
MONGO_CO='auctions'

# Crawl responsibly by identifying yourself (and your website) on the user-agent
#USER_AGENT = 'taobaosearch (+http://www.yourdomain.com)'

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
#    'taobaosearch.middlewares.TaobaosearchSpiderMiddleware': 543,
#}

# Enable or disable downloader middlewares
# See https://doc.scrapy.org/en/latest/topics/downloader-middleware.html
DOWNLOADER_MIDDLEWARES = {
   'taobaosearch.middlewares.TaobaosearchDownloaderMiddleware': 543,
}

# Enable or disable extensions
# See https://doc.scrapy.org/en/latest/topics/extensions.html
#EXTENSIONS = {
#    'scrapy.extensions.telnet.TelnetConsole': None,
#}

# Configure item pipelines
# See https://doc.scrapy.org/en/latest/topics/item-pipeline.html
ITEM_PIPELINES = {
   'taobaosearch.pipelines.TaobaosearchPipeline': 300,
}

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
