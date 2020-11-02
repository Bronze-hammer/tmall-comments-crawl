import scrapy


class CommentscrawlSpider(scrapy.Spider):
    name = 'commentsCrawl'
    allowed_domains = ['tmall.com']
    start_urls = ['http://tmall.com/']

    def parse(self, response):
        pass
