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

# item piplelines settings
ITEM_PIPELINES = { 
    'nestia.pipelines.CosmosPipeline' : 300, 
}

# user agent settings
USER_AGENT = 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/73.0.3683.103 Safari/537.36'

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

# Disable cookies (enabled by default)
COOKIES_ENABLED = True

# Override the default request headers:
DEFAULT_REQUEST_HEADERS = {
    'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8',
    'User-Agent': USER_AGENT,
    'Connection': 'Keep-Alive',
    'Accept-Encoding': 'gzip, deflate',
    'Accept-Language': 'en-US,*',
}

# Cosmos db settings:
COSMOSDB_URL = ''
COSMOSDB_USERNAME = 'apollo1984'
COSMOSDB_KEY = ''
COSMOSDB_DATABASE = 'nestia'
COSMOSDB_COLLECTION = 'sale_properties'

# sale properties:
SALE_PROPERTIES_LIMIT = 500

# http error handling
HTTPERROR_ALLOW_ALL = True