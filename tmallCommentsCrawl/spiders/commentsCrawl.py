import scrapy


class CommentscrawlSpider(scrapy.Spider):
    name = 'commentsCrawl'
    allowed_domains = ['tmall.com']
    start_urls = ['https://detail.tmall.com/item.htm?spm=a1z10.3-b-s.w4011-15493768257.69.36cb30e8TaJe63&id=625746717520&rn=29c9c4da824d6c3934e736fb08e3ba59&abbucket=20']

    def parse(self, response):
        bodys = response.css('div.rate-grid > table > tbody')
        for body in bodys:
            print(body.css('div.tm-rate-fulltxt::text').extract_first().strip())
            break
