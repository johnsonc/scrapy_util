# https://github.com/scrapy/scrapy/blob/master/scrapy/contrib/downloadermiddleware/useragent.py
from scrapy.contrib.downloadermiddleware.useragent import UserAgentMiddleware
import random

# in your settings.py
# DOWNLOADER_MIDDLEWARES = {
#     'scrapy.contrib.downloadermiddleware.useragent.UserAgentMiddleware': None,
#     'bot_name.scrapy_util.downloadermiddleware.rotate_useragent.RotateUserAgentMiddleware': 500,
# }

class RotateUserAgentMiddleware(UserAgentMiddleware):

    def process_request(self, request, spider):
        self.user_agent = random.choice(self.user_agents)
        super(RotateUserAgentMiddleware, self).process_request(request, spider)

    # copied from http://www.useragentstring.com/pages/useragentstring.php
    user_agents = [\
        "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_9_0) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/32.0.1664.3 Safari/537.36",
        "Mozilla/5.0 (Windows NT 6.2; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/32.0.1667.0 Safari/537.36",
        "Mozilla/5.0 (Windows NT 5.1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/31.0.1650.16 Safari/537.36",
        "Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/31.0.1623.0 Safari/537.36",
        "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_6_8) AppleWebKit/537.13+ (KHTML, like Gecko) Version/5.1.7 Safari/534.57.2",
        "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_7_3) AppleWebKit/534.55.3 (KHTML, like Gecko) Version/5.1.3 Safari/534.53.10",
        "Mozilla/5.0 (Windows NT 6.1; Win64; x64; rv:25.0) Gecko/20100101 Firefox/25.0",
        "Mozilla/5.0 (Macintosh; Intel Mac OS X 10.6; rv:25.0) Gecko/20100101 Firefox/25.0",
        "Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:24.0) Gecko/20100101 Firefox/24.0",
        "Mozilla/5.0 (Windows NT 6.0; WOW64; rv:24.0) Gecko/20100101 Firefox/24.0",
        "Mozilla/5.0 (Macintosh; Intel Mac OS X 10.8; rv:24.0) Gecko/20100101 Firefox/24.0"
    ]