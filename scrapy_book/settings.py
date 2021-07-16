# -*- coding: utf-8 -*-

# Scrapy settings for scrapy_book project
#
# For simplicity, this file contains only settings considered important or
# commonly used. You can find more settings consulting the documentation:
#
#     https://doc.scrapy.org/en/latest/topics/settings.html
#     https://doc.scrapy.org/en/latest/topics/downloader-middleware.html
#     https://doc.scrapy.org/en/latest/topics/spider-middleware.html

BOT_NAME = 'scrapy_book'

SPIDER_MODULES = ['scrapy_book.spiders']
NEWSPIDER_MODULE = 'scrapy_book.spiders'

USER_AGENT = 'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/55.0.2883.8 Safari/537.36'

# Crawl responsibly by identifying yourself (and your website) on the user-agent
#USER_AGENT = 'scrapy_book (+http://www.yourdomain.com)'

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
DEFAULT_REQUEST_HEADERS = {
    'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8',
    'Accept-Language': 'en',
    "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_3) AppleWebKit/537.36 (KHTML, li"
                  "ke Gecko) Chrome/81.0.4044.138 Safari/537.36",
    "Cookie": "t=f18d672f5f02333283361f7a027faf6a; cna=pfevF4KruwMCATFGNZqulgP/; cookie2=15ddfbbb62a80754706e020499dd1e73; v=0; _samesite_flag_=true; sgcookie=EINz448jeiIKB8WGxzs9N; uc3=id2=UNDVc8%2F7VdzE9Q%3D%3D&lg2=Vq8l%2BKCLz3%2F65A%3D%3D&nk2=0%2BGi4p5HRSmLlP4%3D&vt3=F8dCufTFCNSqkiy4xCI%3D; csg=72aefe12; lgc=%5Cu554A941826670; dnk=%5Cu554A941826670; skt=3860c595dca8d168; existShop=MTU5NzcxMDE4OQ%3D%3D; uc4=nk4=0%400VrwPsxHxKlIRxHYn8ykawwoZ9uFVQ%3D%3D&id4=0%40UgclHutHCO6ZuzWz2MpkPDjGN4DT; tracknick=%5Cu554A941826670; _cc_=V32FPkk%2Fhw%3D%3D; enc=Cb6iMnjgmA9xnM3tVujqJ9wsNaWy5aqhGOIdZ8X1hEjHsNwahsNbxuAaBm%2B0UgqwdOl7ZGHdobezDfdX8fdEIA%3D%3D; mt=ci=1_1; thw=cn; hng=CN%7Czh-CN%7CCNY%7C156; alitrackid=www.taobao.com; lastalitrackid=www.taobao.com; _m_h5_tk=798da7f33bdf9cb44e2c7d98ce2bdb39_1597840452252; _m_h5_tk_enc=fe629ed25401362d32eb5661ee558ee1; _tb_token_=e518fe307f878; uc1=cookie21=UtASsssmeWzt&cookie14=UoTV6yHCSQX2uw%3D%3D&cookie16=W5iHLLyFPlMGbLDwA%2BdvAGZqLg%3D%3D&existShop=false&pas=0; _uab_collina=159783978023357089252779; x5sec=7b227365617263686170703b32223a226637393930633138333334643634356630393863363866303562383962626563434b4f7a39506b46454c7661382b534f685a537a42686f4d4d7a41784d5467324f4467794d547378227d; JSESSIONID=81ED84AB340E7E67228ACDA5715389D8; isg=BHZ2n7zRNfwll8EU9uMJSqY0x6p4l7rRV0w-0eBfaNn0Ixa9SCPY4dXSP_9Pi7Lp; l=eBOQeAxlOI8AcCX-BOfZnurza77TIIRAguPzaNbMiOCPO25p5CjRWZuI2-T9CnGVh6jBR3oPlnYkBeYBc3K-nxv92j-la6kmn; tfstk=ctjdB7tTXRHL9wvO3wUMF2PMVnwGZmU9a2Om2-IUleEQ2IoRi5scDW5adKGpXRC.."

}

# Enable or disable spider middlewares
# See https://doc.scrapy.org/en/latest/topics/spider-middleware.html
#SPIDER_MIDDLEWARES = {
#    'scrapy_book.middlewares.ScrapyBookSpiderMiddleware': 543,
#}

# Enable or disable downloader middlewares
# See https://doc.scrapy.org/en/latest/topics/downloader-middleware.html
#DOWNLOADER_MIDDLEWARES = {
#    'scrapy_book.middlewares.ScrapyBookDownloaderMiddleware': 543,
#}

# Enable or disable extensions
# See https://doc.scrapy.org/en/latest/topics/extensions.html
#EXTENSIONS = {
#    'scrapy.extensions.telnet.TelnetConsole': None,
#}

# Configure item pipelines
# See https://doc.scrapy.org/en/latest/topics/item-pipeline.html
ITEM_PIPELINES = {
   'scrapy_book.pipelines.ScrapyBookPipeline': 300,
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
