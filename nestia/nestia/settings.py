# -*- coding: utf-8 -*-

# Scrapy settings for nestia project
#
# For simplicity, this file contains only settings considered important or
# commonly used. You can find more settings consulting the documentation:
#
#     https://doc.scrapy.org/en/latest/topics/settings.html
#     https://doc.scrapy.org/en/latest/topics/downloader-middleware.html
#     https://doc.scrapy.org/en/latest/topics/spider-middleware.html

BOT_NAME = 'nestia'

SPIDER_MODULES = ['nestia.spiders']
NEWSPIDER_MODULE = 'nestia.spiders'

ITEM_PIPELINES = { 
    'nestia.pipelines.CosmosPipeline' : 300, 
}

USER_AGENT = 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/73.0.3683.103 Safari/537.36'

# Crawl responsibly by identifying yourself (and your website) on the user-agent
#USER_AGENT = 'nestia (+http://www.yourdomain.com)'

# Obey robots.txt rules
#ROBOTSTXT_OBEY = True
ROBOTSTXT_OBEY = False

# Configure maximum concurrent requests performed by Scrapy (default: 16)
CONCURRENT_REQUESTS = 1

# Configure a delay for requests for the same website (default: 0)
# See https://doc.scrapy.org/en/latest/topics/settings.html#download-delay
# See also autothrottle settings and docs
DOWNLOAD_DELAY = 10
RANDOMIZE_DOWNLOAD_DELAY = True

# The download delay setting will honor only one of:
#CONCURRENT_REQUESTS_PER_DOMAIN = 16
#CONCURRENT_REQUESTS_PER_IP = 16

# Disable cookies (enabled by default)
COOKIES_ENABLED = True

# Disable Telnet Console (enabled by default)
#TELNETCONSOLE_ENABLED = False

# Override the default request headers:
DEFAULT_REQUEST_HEADERS = {
    'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8',
    'User-Agent': USER_AGENT,
    'Connection': 'Keep-Alive',
    'Accept-Encoding': 'gzip, deflate',
    'Accept-Language': 'en-US,*',
}

# Cosmos db settings:
COSMOSDB_URL = 'mongodb://apollo1984:jlNDjCFRJLLh80k7aaGpyqLqhZ5XHXvPjjvKjp1GpdyIP8SHplQOZ6pGrH7FtHmEZ7J1CMjIkxYyIGSwhY6MQA==@apollo1984.documents.azure.com:10255/?ssl=true&replicaSet=globaldb'
#COSMOSDB_HOST = 'https://localhost:8081'
COSMOSDB_USERNAME = 'apollo1984'
COSMOSDB_KEY = 'jlNDjCFRJLLh80k7aaGpyqLqhZ5XHXvPjjvKjp1GpdyIP8SHplQOZ6pGrH7FtHmEZ7J1CMjIkxYyIGSwhY6MQA=='
COSMOSDB_DATABASE = 'nestia'
COSMOSDB_COLLECTION = 'sale_properties'

# sale properties:
SALE_PROPERTIES_LIMIT = 500

HTTPERROR_ALLOW_ALL = True

# Enable or disable spider middlewares
# See https://doc.scrapy.org/en/latest/topics/spider-middleware.html
#SPIDER_MIDDLEWARES = {
#    'nestia.middlewares.NestiaSpiderMiddleware': 543,
#}

# Enable or disable downloader middlewares
# See https://doc.scrapy.org/en/latest/topics/downloader-middleware.html
#DOWNLOADER_MIDDLEWARES = {
#    'nestia.middlewares.NestiaDownloaderMiddleware': 543,
#}

# Enable or disable extensions
# See https://doc.scrapy.org/en/latest/topics/extensions.html
#EXTENSIONS = {
#    'scrapy.extensions.telnet.TelnetConsole': None,
#}

# Configure item pipelines
# See https://doc.scrapy.org/en/latest/topics/item-pipeline.html
#ITEM_PIPELINES = {
#    'nestia.pipelines.NestiaPipeline': 300,
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
