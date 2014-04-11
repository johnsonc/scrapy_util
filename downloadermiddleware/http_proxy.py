# in your settings.py
# DOWNLOADER_MIDDLEWARES = {
#     'scrapy.contrib.downloadermiddleware.httpproxy.HttpProxyMiddleware': None,
#     'bot_name.scrapy_util.downloadermiddleware.http_proxy.HttpProxyMiddleware': 751 
# }
# HTTP_PROXY = "http://127.0.0.1:9050"


class HttpProxyMiddleware(object):

    def __init__(self, settings):
        self.settings = settings

    @classmethod
    def from_crawler(cls, crawler):
        return cls(crawler.settings)

    def process_request(self, request, spider):
        http_proxy = self.settings.get('HTTP_PROXY')
        if http_proxy:
            request.meta['proxy'] = http_proxy