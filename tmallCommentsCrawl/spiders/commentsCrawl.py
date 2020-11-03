import scrapy


class CommentscrawlSpider(scrapy.Spider):
    name = 'commentsCrawl'
    allowed_domains = ['detail.tmall.com']
    start_urls = [
        'https://detail.tmall.com/item.htm?spm=a1z10.3-b-s.w5001-21647916242.5.611830e8CALfIx&id=617954262029&rn=7ce83012541598e5a3a6b406eeb18248&abbucket=1&skuId=4478575424436&scene=taobao_shop'
    ]

    def parse(self, response):
        bodys = response.css('div.rate-grid > table > tbody');
        for body in bodys:
            yield {
                'comment' : body.css('div.tm-rate-fulltxt::text')
            }
