import scrapy


class GovSpider(scrapy.Spider):
    name = 'gov'
    allowed_domains = ['www.gov.br']
    start_urls = ['http://www.gov.br/']

    def parse(self, response):
        pass
