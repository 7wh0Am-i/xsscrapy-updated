# -*- coding: utf-8 -*-

# Scrapy settings for xsscrapy project

# Uncomment below in order to disallow redirects
#REDIRECT_ENABLED = False

# Uncomment this to lessen the spider's output
#LOG_LEVEL = 'INFO'

BOT_NAME = 'xsscrapy'

SPIDER_MODULES = ['xsscrapy.spiders']
NEWSPIDER_MODULE = 'xsscrapy.spiders'

# For adding javascript rendering
#DOWNLOAD_HANDLERS = {'http':'xsscrapy.scrapyjs.dhandler.WebkitDownloadHandler',
#                     'https': 'xsscrapy.scrapyjs.dhandler.WebkitDownloadHandler'}

# Configure maximum concurrent requests performing at the same time
CONCURRENT_REQUESTS = 30

# Configure a delay for requests for the same website
DOWNLOAD_DELAY = 0

# Enable or disable downloader middlewares
DOWNLOADER_MIDDLEWARES = {
    'xsscrapy.middlewares.InjectedDupeFilter': 100,
    'xsscrapy.middlewares.RandomUserAgentMiddleware': 200,
    'scrapy.downloadermiddlewares.httpauth.HttpAuthMiddleware': 300,
}

# Enable or disable spider middlewares
SPIDER_MIDDLEWARES = {
    'scrapy.spidermiddlewares.httperror.HttpErrorMiddleware': 50,
}

# Configure item pipelines
ITEM_PIPELINES = {
    'xsscrapy.pipelines.XSSCharFinder': 100,
}

# Enable and configure HTTP caching
HTTPCACHE_ENABLED = True
HTTPCACHE_EXPIRATION_SECS = 86400  # 24 hours
HTTPCACHE_DIR = 'httpcache'
HTTPCACHE_IGNORE_HTTP_CODES = [503, 504, 505, 500, 502, 429]
HTTPCACHE_STORAGE = 'scrapy.extensions.httpcache.FilesystemCacheStorage'

# Enable and configure logging
LOG_LEVEL = 'INFO'
LOG_FORMAT = '%(asctime)s [%(name)s] %(levelname)s: %(message)s'

# Configure maximum requests performing at the same time to the same domain
CONCURRENT_REQUESTS_PER_DOMAIN = 30

# Enable or disable cookies
COOKIES_ENABLED = True
#COOKIES_DEBUG = True

# Prevent duplicate link crawling
# Bloom filters are way more memory efficient than just a hash lookup
DUPEFILTER_CLASS = 'xsscrapy.bloomfilters.BloomURLDupeFilter'
#DUPEFILTER_CLASS = 'scrapy.dupefilter.RFPDupeFilter'

# Configure item exporters
FEED_EXPORT_ENCODING = 'utf-8'

# Set settings whose default value is deprecated to a future-proof value
REQUEST_FINGERPRINTER_IMPLEMENTATION = "2.7"
TWISTED_REACTOR = "twisted.internet.asyncio.AsyncioSelectorReactor"
FEED_EXPORT_HANDLERS = {
    "json": "scrapy.exporters.JsonItemExporter",
    "jsonlines": "scrapy.exporters.JsonLinesItemExporter",
    "csv": "scrapy.exporters.CsvItemExporter",
}

# Bloom filter settings
BLOOMFILTER_SIZE = 300000
